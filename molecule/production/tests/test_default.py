import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("name", [
    'shadow-utils', 'util-linux', 'net-tools',
    'initscripts', 'sudo', 'git', 'unzip', 'java-1.8.0-openjdk.x86_64'
    ])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_tomcat_service(host):
    service = host.service("tomcat")
    assert service.is_running
