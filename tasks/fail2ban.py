"""
fail2ban configuration for VPS security
Equivalent to ansible role-common/tasks/fail2ban.yml
"""

from pyinfra.operations import apt, files, systemd

# Install fail2ban and ruby
apt.packages(
    name="Install fail2ban and ruby",
    packages=["fail2ban", "ruby"],
    present=True,
    _sudo=True,
)

# Copy jail.local configuration file
files.put(
    name="Copy jail.local configuration",
    src="tasks/tmpl/etc/fail2ban/jail.local",
    dest="/etc/fail2ban/jail.local",
    user="root",
    group="root",
    mode="644",
    _sudo=True,
)

# Restart fail2ban service
systemd.service(
    name="Restart fail2ban service",
    service="fail2ban",
    restarted=True,
    enabled=True,
    _sudo=True,
)