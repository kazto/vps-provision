"""Test that fail2ban from fail2ban.py is installed and configured"""

import testinfra


def test_fail2ban_installed_and_configured(host):
    """Test that fail2ban from fail2ban.py is installed and configured"""
    # Packages should be installed
    assert host.package("fail2ban").is_installed, "fail2ban should be installed"
    
    # Configuration file should exist
    jail_config = host.file("/etc/fail2ban/jail.local")
    assert jail_config.exists, "fail2ban jail.local config should exist"
    assert jail_config.user == "root", "jail.local should be owned by root"
    assert jail_config.group == "root", "jail.local should be owned by root group"
    assert jail_config.mode == 0o644, "jail.local should have 644 permissions"
    
    # Service should be running and enabled
    fail2ban_service = host.service("fail2ban")
    assert fail2ban_service.is_running, "fail2ban service should be running"
    assert fail2ban_service.is_enabled, "fail2ban service should be enabled"