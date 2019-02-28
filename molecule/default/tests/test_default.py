import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('openjdk-8-jre'),
    ('subsonic'),
])
def test_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_service_is_running(host):
    service = host.service('subsonic')
    assert service.is_running


def test_service_is_enabled(host):
    service = host.service('subsonic')
    assert service.is_enabled
