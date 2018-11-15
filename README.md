# Typesafe Activator

Installs Typesafe Activator

[![Build Status](https://travis-ci.org/rgibert/ansible-role-typesafe-activator.svg?branch=master)](https://travis-ci.org/rgibert/ansible-role-typesafe-activator)
[![GitHub issues](https://img.shields.io/github/issues/rgibert/ansible-role-typesafe-activator.svg)](https://github.com/rgibert/ansible-role-typesafe-activator/issues)
[![GitHub forks](https://img.shields.io/github/forks/rgibert/ansible-role-typesafe-activator.svg)](https://github.com/rgibert/ansible-role-typesafe-activator/network)
[![GitHub stars](https://img.shields.io/github/stars/rgibert/ansible-role-typesafe-activator.svg)](https://github.com/rgibert/ansible-role-typesafe-activator/stargazers)
[![GitHub license](https://img.shields.io/github/license/rgibert/ansible-role-typesafe-activator.svg)](https://github.com/rgibert/ansible-role-typesafe-activator/blob/master/LICENSE)

## Requirements

- none

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| typesafe_activator_dl_checksum | sha256:3740355ce4d4c099b9349704dc5851341e731981b25094b7b7dcefe7eceff530 | SHA256 checksum of download zip |
| typesafe_activator_dl_uri | https://downloads.typesafe.com/typesafe-activator/{{ typesafe_activator_version }}/typesafe-activator-{{ typesafe_activator_version }}.zip | URI to download from |
| typesafe_activator_group | root | |
| typesafe_activator_install_root | /usr/local/share | Root path to install to |
| typesafe_activator_user | root | |
| typesafe_activator_version | 1.3.12 | Version of typesafe-activator to install |

## Dependencies

- none

## Example Playbook

```yaml
- hosts:
    - servers
  roles:
    - rgibert.typesafe_activator
```

## License

GPLv3

## Author Information

Richard Gibert
[richard@gibert.ca](mailto:richard@gibert.ca)
[https://richard.gibert.ca](https://richard.gibert.ca/)
