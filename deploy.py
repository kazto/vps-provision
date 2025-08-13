#!/usr/bin/env python3
"""
Main deployment script for VPS provisioning
Equivalent to Ansible's main playbook
"""

from pyinfra import config
from pyinfra.operations import server, files

# Import task modules
from tasks import base, fail2ban, logwatch, postfix, docker, cronapt

# Global configuration
config.SUDO = True
config.USE_SUDO_LOGIN = True
config.SUDO_USER = "root"

# Basic server setup - equivalent to setup.yml
def setup_basic_server():
    """Basic server hardening and user setup"""
    
    # Create user kazto
    server.user(
        name="Create user kazto",
        user="kazto",
        present=True,
        home="/home/kazto",
        shell="/bin/bash",
        _sudo=True,
    )
    
    # Disable root SSH login
    files.line(
        name="Disable root SSH login",
        path="/etc/ssh/sshd_config",
        line="PermitRootLogin no",
        replace="^PermitRootLogin.*",
        _sudo=True,
    )
    
    # Restart SSH service
    server.service(
        name="Restart SSH service",
        service="ssh",
        restarted=True,
        _sudo=True,
    )

# Common tasks deployment - equivalent to role-common
def deploy_common():
    """Deploy common system configuration"""
    
    # Import and execute task modules
    import tasks.base
    import tasks.fail2ban
    import tasks.logwatch
    import tasks.postfix
    import tasks.cronapt
    import tasks.docker

# Mastodon deployment - equivalent to role-mastodon
def deploy_mastodon():
    """Deploy Mastodon application"""
    
    # Create mastodon user and group
    server.group(
        name="Create mastodon group",
        group="mastodon",
        gid=991,
        present=True,
        _sudo=True,
    )
    
    server.user(
        name="Create mastodon user", 
        user="mastodon",
        group="mastodon",
        groups=["staff", "docker"],
        uid=991,
        home="/opt/mastodon",
        shell="/usr/sbin/nologin",
        create_home=True,
        present=True,
        _sudo=True,
    )
    
    # Clone Mastodon repository
    server.shell(
        name="Clone Mastodon repository",
        commands=[
            "git clone https://github.com/mastodon/mastodon.git /opt/mastodon/live",
            "chown -R mastodon:mastodon /opt/mastodon/live"
        ],
        _sudo=True,
    )

if __name__ == "__main__":
    # Execute deployment phases
    setup_basic_server()
    deploy_common() 
    # deploy_mastodon()