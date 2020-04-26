# Ansible Role: NTP

[![Build Status](https://img.shields.io/travis/arillso/ansible.ntp.svg?branch=master&style=popout-square)](https://travis-ci.org/arillso/ansible.ntp) [![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=popout-square)](https://sbaerlo.ch/licence) [![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-ntp-blue.svg?style=popout-square)](https://galaxy.ansible.com/arillso/ntp) [![Ansible Role](https://img.shields.io/ansible/role/d/21608.svg?style=popout-square)](https://galaxy.ansible.com/arillso/ntp)

## Description

The role configures and installs NTP under Linux and Windows. It is possible to specify multiple NTP servers for time synchronization. For Linux this is done via the NTP package, for Windows it is set up via the local GPO for the NTP synchronization.

## Installation

```bash
ansible-galaxy install arillso.ntp
```

## Requirements

This role require Ansible 2.7 or higher. The platform requirements are listed in the metadata file.

## Role Variables

### NTP Server

List of NTP servers for time synchronization. Special case if an inventory group NAS is present it will be taken as the first NTP server.

```yml
ntp_server:
  - "{{ groups['NAS'] | default('0.pool.ntp.org') }}"
  - '1.pool.ntp.org'
  - '2.pool.ntp.org'
  - '3.pool.ntp.org'
```

### Linux

#### Restrictions

Restrictions are used to control access to your ntpd:

```yml
ntp_config_restrict:
  - '-4 default kod notrap nomodify nopeer noquery'
  - '-6 default kod notrap nomodify nopeer noquery'
  - '127.0.0.1'
  - '::1'
```

#### Listen

Specifies to which interface NTP should be appended:

```yml
ntp_config_listen: []
```

#### More

NTP configurations details:

```yml
ntp_config_filegen:
- 'loopstats file loopstats type day enable'
- 'peerstats file peerstats type day enable'
- 'clockstats file clockstats type day enable'

  ntp_config_statistics: 'loopstats peerstats clockstats'
  ntp_config_crypto: ''
  ntp_config_includefile: ''
  ntp_config_keys: ''
  ntp_config_trustedkey: ''
  ntp_config_requestkey: ''
  ntp_config_controlkey: ''
  ntp_config_broadcast: ''
  ntp_config_broadcastclient: ''
  ntp_config_multicastclient: ''
  ntp_config_tinker_panic_enabled: ''
```

### Windows

Specifies if the time server is configured via Windows GPO so that it is not permanently overwritten.

#### GPO

```yml
ntp_GPO_enable: '{{ default_GPO_enable | default(false) }}'
```

#### NTP Settings

Possible settings are described under the following [link](https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsTimeService::W32TIME_POLICY_CONFIGURE_NTPCLIENT)

```yml
ntp_time_type: 'NTP'
ntp_crosssitesyncflags: '2'
ntp_resolvepeerbackoffminutes: '15'
ntp_resolvepeerbackoffmaxtimes: '7'
ntp_specialpollinterval: '1024'
ntp_eventlogflags: '0'
```

#### NTP Flags

Possible NTP flags that can be used under windows.
0x01 SpecialInterval
0x02 UseAsFallbackOnly
0x04 SymmatricActive
0x08 Client

```yml
ntp_flag: '0x01'
```

## Dependencies

None

## Author

- Benno Joy
- René Moser
- [Simon Bärlocher](https://sbaerlocher.ch)

## License

BSD
