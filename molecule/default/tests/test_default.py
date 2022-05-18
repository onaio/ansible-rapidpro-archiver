import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rapidpro_archiver_service(host):
    rapidpro_archiver = host.service("rapidpro-archiver")

    assert rapidpro_archiver.is_running
    assert rapidpro_archiver.is_enabled


def test_rapidpro_archiver_app_files(host):
    appDir = host.file("/home/rapidpro-archiver/app")
    assert appDir.exists
    assert appDir.user == "rapidpro-archiver"
    assert appDir.group == "rapidpro-archiver"
    assert appDir.is_symlink
    assert appDir.linked_to == "/home/rapidpro-archiver/app-versioned/5.6.0"

    appVersionedDir = host.file("/home/rapidpro-archiver/app-versioned/5.6.0")
    assert appVersionedDir.exists
    assert appVersionedDir.user == "rapidpro-archiver"
    assert appVersionedDir.group == "rapidpro-archiver"
    assert appVersionedDir.is_directory
    assert oct(appVersionedDir.mode) == "0o755"

    configFile = host.file("/home/rapidpro-archiver/app/archiver.toml")
    assert configFile.exists
    assert configFile.user == "rapidpro-archiver"
    assert configFile.group == "rapidpro-archiver"
    assert configFile.is_file
    assert oct(configFile.mode) == "0o750"
