# Ansible Role: Subsonic

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-subsonic.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-subsonic)

An Ansible Role that installs [Subsonic](http://subsonic.org) on Debian and Ubuntu.

## Requirements

None.

## Role Variables

None.

# Dependencies

None.

# Example Playbook

```yaml
- name: Install Subsonic
  hosts: all
  become: true
  roles:
    - hadrienpatte.subsonic
```

## License

MIT

## Author Information

Hadrien Patte [![PGP 0xFB500BB0](https://peegeepee.com/badge/orange/FB500BB0.svg)](https://peegeepee.com/FB500BB0)
