"""
postfix mail server configuration
Equivalent to ansible role-common/tasks/postfix.yml
"""

from pyinfra.operations import apt, files, server, systemd
from pyinfra import host

# Copy debconf preselection file
files.put(
    name="Copy debconf-set-selections",
    src="tasks/tmpl/tmp/debconf-set-selections.tmp",
    dest="/tmp/debconf-set-selections.tmp",
    mode="644",
)

# Apply debconf selections
server.shell(
    name="Apply debconf selections",
    commands=["debconf-set-selections /tmp/debconf-set-selections.tmp"],
)

# Install postfix and related packages
apt.packages(
    name="Install postfix packages",
    packages=["postfix", "libsasl2-modules", "mailutils", "ruby"],
    present=True,
)

# Get configuration from host data
aws_ses_region = host.data.get("aws_ses_region", "us-east-1")
aws_ses_username = host.data.get("aws_ses_username", "")
aws_ses_password = host.data.get("aws_ses_password", "")
ses_relay_host = host.data.get("ses_relay_host", f"email-smtp.{aws_ses_region}.amazonaws.com")

# Setup SASL password file
files.template(
    name="Setup SASL password file",
    src="tasks/tmpl/etc/postfix/sasl_passwd.j2",
    dest="/etc/postfix/sasl_passwd",
    user="root",
    group="root", 
    mode="600",
    ses_relay_host=ses_relay_host,
    aws_ses_username=aws_ses_username,
    aws_ses_password=aws_ses_password,
)

# Encode password file
server.shell(
    name="Encode SASL password file",
    commands=["postmap /etc/postfix/sasl_passwd"],
)

# Copy main.cf modification script
files.put(
    name="Copy main.cf modification script",
    src="tasks/tmpl/etc/postfix/modify-maincf.rb",
    dest="/etc/postfix/modify-maincf.rb",
    mode="755",
)

# Modify main.cf configuration
server.shell(
    name="Modify main.cf configuration", 
    commands=[
        "cd /etc/postfix && ruby modify-maincf.rb main.cf > main.cf.tmp && mv main.cf.tmp main.cf"
    ],
)

# Cleanup modification script
files.file(
    name="Remove modification script",
    path="/etc/postfix/modify-maincf.rb",
    present=False,
)

# Restart postfix service
systemd.service(
    name="Restart postfix service",
    service="postfix",
    restarted=True,
    enabled=True,
)