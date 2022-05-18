onaio - RapidPro Archiver [![Build Status](https://github.com/onaio/ansible-rapidpro-archiver/workflows/CI/badge.svg)](https://github.com/onaio/ansible-rapidpro-archiver/actions?query=workflow%3ACI)
=========

Installs and configures [RapidPro Archiver](https://github.com/nyaruka/rp-archiver).

Requirements
------------

RapidPro Archiver needs to point to instances of Elasticsearch and PostgreSQL for it to run as expected.

Role Variables
--------------
Check the [defaults/main.yml](./defaults/main.yml) file for the full list of default variables.

```yml
# System architecture for the host. Possible value are:
#   - linux_amd64
#   - darwin_amd64
rapidpro_archiver_system_architecture: "linux_amd64"

# The package repository to download RapidPro Archiver tarballs from
rapidpro_archiver_download_url: "https://github.com/nyaruka/rp-archiver/releases/download/v{{ rapidpro_archiver_version }}/rp-archiver_{{ rapidpro_archiver_version }}_{{ rapidpro_archiver_system_architecture }}.tar.gz"

# The root directory RapidPro Archiver versioned directories are created
rapidpro_archiver_package_directory_root: "{{ rapidpro_archiver_system_home }}/app-versioned"

# The name to give the directory the RapidPro Archiver binary is copied to
rapidpro_archiver_package_directory_name: "{{ rapidpro_archiver_version }}"

```

Dependencies
------------

Example Playbook
----------------

```yml
- hosts: all
  roles:
    - role: postgresql
    - role: ansible-rapidpro-archiver
      rapidpro_archiver_version: "7.2.0"
```

License
-------

Apache v2.0
