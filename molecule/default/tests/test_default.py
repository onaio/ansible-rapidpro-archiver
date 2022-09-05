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
    assert appDir.linked_to == "/home/rapidpro-archiver/app-versioned/7.2.0"

    appVersionedDir = host.file("/home/rapidpro-archiver/app-versioned/7.2.0")
    assert appVersionedDir.exists
    assert appVersionedDir.user == "rapidpro-archiver"
    assert appVersionedDir.group == "rapidpro-archiver"
    assert appVersionedDir.is_directory
    assert oct(appVersionedDir.mode) == "00755"

    envfile = host.file("/home/rapidpro-archiver/app/environment")
    assert envfile.exists
    assert envfile.user == "rapidpro-archiver"
    assert envfile.group == "rapidpro-archiver"
    assert envfile.is_file
    assert oct(envfile.mode) == "00750"
