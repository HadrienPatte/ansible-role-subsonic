# Ansible Role: Subsonic

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-subsonic.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-subsonic)

An Ansible Role that installs [Subsonic](http://subsonic.org) on Debian and
Ubuntu.

## Requirements

None.

## Role Variables

* `subsonic_version`: version to download, defaults to `6.1.5`
* `subsonic_port`: HTTP port Subsonic should bind to, defaults to `4040`
* `subsonic_FQDN`: Fully Qualified Domain Name of the server
* `subsonic_HTTP_server`: HTTP reverse proxy server, possible values are
  `apache2` and `nginx`, defaults to `nginx`
* `subsonic_certificate_path`: directory where the TSL/SSL certificate will be
* `subsonic_remove_default`: set this to `true` to remove apache2/nginx default
  site

# Dependencies

* [hadrienpatte.self_signed_certificate](https://galaxy.ansible.com/hadrienpatte/self_signed_certificate)

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
