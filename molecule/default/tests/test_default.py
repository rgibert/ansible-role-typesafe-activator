import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_installed(host):
    assert host.file("/usr/local/share/activator-dist-1.3.12").exists
    assert host.file("/usr/local/share/typesafe-activator").exists
