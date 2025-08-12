"""
logwatch configuration for log monitoring
Equivalent to ansible role-common/tasks/logwatch.yml
"""

from pyinfra.operations import apt, files, server
from pyinfra import host

# Install logwatch and ruby
apt.packages(
    name="Install logwatch and ruby",
    packages=["logwatch", "ruby"],
    present=True,
)

# Copy default configuration
files.get(
    name="Copy default logwatch configuration",
    src="/usr/share/logwatch/default.conf/logwatch.conf",
    dest="/etc/logwatch/conf/logwatch.conf",
)

# Copy modification script
files.put(
    name="Copy logwatch modification script",
    src="tasks/tmpl/etc/logwatch/modify-logwatch.rb",
    dest="/etc/logwatch/conf/modify-logwatch.rb",
    mode="755",
)

# Get configuration from host data
logwatch_mailto = host.data.get("logwatch_mailto", "")
logwatch_mailfrom = host.data.get("logwatch_mailfrom", "")

# Modify logwatch configuration
server.shell(
    name="Modify logwatch configuration",
    commands=[
        f"cd /etc/logwatch/conf && ruby modify-logwatch.rb logwatch.conf {logwatch_mailto} {logwatch_mailfrom} > logwatch.conf.tmp && mv logwatch.conf.tmp logwatch.conf"
    ],
)

# Cleanup modification script
files.file(
    name="Remove modification script",
    path="/etc/logwatch/conf/modify-logwatch.rb",
    present=False,
)