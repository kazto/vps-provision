"""Test that all tasks in /tasks directory were executed successfully"""

import testinfra


def test_base_packages_installed(host):
    """Test that base packages from base.py are installed"""
    base_packages = [
        "curl", "git", "vim", "tmux", "zsh", "build-essential",
        "libssl-dev", "libreadline-dev", "zlib1g-dev", "libncurses5-dev",
        "libffi-dev", "libgdbm-dev", "libdb-dev", "libbz2-dev", "liblzma-dev",
        "libsqlite3-dev", "libxml2-dev", "libxslt1-dev", "libyaml-dev"
    ]
    
    for package in base_packages:
        assert host.package(package).is_installed, f"Base package {package} should be installed"


def test_docker_installed_and_running(host):
    """Test that Docker from docker.py is installed and running"""
    # Docker package should be installed
    assert host.package("docker.io").is_installed, "Docker package should be installed"
    
    # Docker service should be running and enabled
    docker_service = host.service("docker")
    assert docker_service.is_running, "Docker service should be running"
    assert docker_service.is_enabled, "Docker service should be enabled"
    
    # Docker command should be available
    assert host.run("docker --version").rc == 0, "Docker command should work"


def test_fail2ban_installed_and_configured(host):
    """Test that fail2ban from fail2ban.py is installed and configured"""
    # Packages should be installed
    assert host.package("fail2ban").is_installed, "fail2ban should be installed"
    assert host.package("ruby").is_installed, "ruby should be installed"
    
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
    
    # Modification script should be removed
    modify_script = host.file("/etc/postfix/modify-maincf.rb")
    assert not modify_script.exists, "Modification script should be removed after execution"


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
    
    # Modification script should be removed
    modify_script = host.file("/etc/logwatch/conf/modify-logwatch.rb")
    assert not modify_script.exists, "Modification script should be removed after execution"
    
    # Logwatch should be executable
    assert host.run("which logwatch").rc == 0, "logwatch command should be available"


def test_services_status(host):
    """Test that all configured services are in expected state"""
    services_should_be_running = [
        "docker",
        "fail2ban", 
        "postfix"
    ]
    
    for service_name in services_should_be_running:
        service = host.service(service_name)
        assert service.is_running, f"Service {service_name} should be running"
        assert service.is_enabled, f"Service {service_name} should be enabled"