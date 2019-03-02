# Ansible Role: Subsonic

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-subsonic.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-subsonic)

An Ansible Role that installs [Subsonic](http://subsonic.org) on Debian and
Ubuntu.

## Requirements

None.

## Role Variables

* `subsonic_version`: version to download, defaults to `6.1.5`
* `subsonic_port`: port on which Subsonic will listen for incoming HTTP traffic,
  defaults to `4040`
* `subsonic_max_memory`: subsonic memory limit (max Java heap size) in
  megabytes, defaults to `100`
* `subsonic_music_folder`: directory where subsonic will look for musics,
  defaults to `/var/music`
* `subsonic_user`: user that will run subsonic
* `subsonic_FQDN`: Fully Qualified Domain Name of the server
* `subsonic_HTTP_server`: HTTP reverse proxy server, possible values are
  `apache2` and `nginx`, defaults to `nginx`
* `subsonic_certificate_path`: directory where the TSL/SSL certificate will be
* `subsonic_generate_self_signed_certificate`: wether to generate a self-signed
  certificate, defaults to `true`. If you set this to `false`, make sure to have
  a certificate and private key in `subsonic_certificate_path`, otherwise the
  role will fail to start the reverse proxy HTTP server.
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
