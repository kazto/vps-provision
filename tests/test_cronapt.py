"""Test that cron-apt from cronapt.py is installed and configured"""

import testinfra


def test_cronapt_installed_and_configured(host):
    """Test that cron-apt from cronapt.py is installed and configured"""
    # Package should be installed
    assert host.package("cron-apt").is_installed, "cron-apt should be installed"
    
    # Configuration file should exist
    config_file = host.file("/etc/cron-apt/config")
    assert config_file.exists, "cron-apt config file should exist"
    
    # Modification script should be removed
    modify_script = host.file("/etc/cron-apt/modify-cronapt.rb")
    assert not modify_script.exists, "Modification script should be removed after execution"
    
    # Cron job should be present
    cron_job = host.file("/etc/cron.d/cron-apt")
    assert cron_job.exists, "cron-apt cron job should exist"