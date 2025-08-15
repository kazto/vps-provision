"""Test that logwatch from logwatch.py is installed and configured"""

import testinfra


def test_logwatch_installed_and_configured(host):
    """Test that logwatch from logwatch.py is installed and configured"""
    # Package should be installed
    assert host.package("logwatch").is_installed, "logwatch should be installed"
    
    # Config directory should exist
    config_dir = host.file("/etc/logwatch/conf")
    assert config_dir.is_directory, "logwatch config directory should exist"
    
    # Configuration file should exist
    config_file = host.file("/etc/logwatch/conf/logwatch.conf")
    assert config_file.exists, "logwatch config file should exist"
    
    # Logwatch should be executable
    assert host.run("which logwatch").rc == 0, "logwatch command should be available"