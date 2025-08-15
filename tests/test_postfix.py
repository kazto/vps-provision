"""Test that postfix from postfix.py is installed and configured"""

import testinfra


def test_postfix_installed_and_configured(host):
    """Test that postfix from postfix.py is installed and configured"""
    # Packages should be installed
    assert host.package("postfix").is_installed, "postfix should be installed"
    assert host.package("libsasl2-modules").is_installed, "libsasl2-modules should be installed"
    assert host.package("mailutils").is_installed, "mailutils should be installed"
    
    # SASL password file should exist and have correct permissions
    sasl_passwd = host.file("/etc/postfix/sasl_passwd")
    assert sasl_passwd.exists, "SASL password file should exist"
    assert sasl_passwd.user == "root", "sasl_passwd should be owned by root"
    assert sasl_passwd.mode == 0o600, "sasl_passwd should have 600 permissions"
    
    # SASL password database should exist
    sasl_passwd_db = host.file("/etc/postfix/sasl_passwd.db")
    assert sasl_passwd_db.exists, "SASL password database should exist"
    
    # Main configuration file should exist
    main_cf = host.file("/etc/postfix/main.cf")
    assert main_cf.exists, "postfix main.cf should exist"
    
    # Service should be running and enabled
    postfix_service = host.service("postfix")
    assert postfix_service.is_running, "postfix service should be running"
    assert postfix_service.is_enabled, "postfix service should be enabled"
    
