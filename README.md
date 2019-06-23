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
* `subsonic_FQDN`: List of Fully Qualified Domain Names of the server
* `subsonic_HTTP_server`: HTTP reverse proxy server, possible values are
  `apache2` and `nginx`, defaults to `nginx`
* `subsonic_certificate_path`: directory where the TSL/SSL certificate will be
* `subsonic_generate_self_signed_certificate`: wether to generate a self-signed
  certificate, defaults to `true`.
* `subsonic_redirect_HTTPS`: set this to `true` to have the reverse proxy
  automatically redirect requests to HTTPS when using self-signed certificate,
  defaults to `false`
* `subsonic_letsencrypt`: set this to `true` to generate TSL/SSL certificate
  with Let's encrypt, defaults to `false`
* `subsonic_letsencrypt_email`: email to use when registering with Let's encrypt
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
