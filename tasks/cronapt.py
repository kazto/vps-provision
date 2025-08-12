"""
cron-apt automatic updates configuration
Equivalent to ansible role-common/tasks/cron-apt.yml
"""

from pyinfra.operations import apt, files, server
from pyinfra import host

# Install cron-apt and ruby
apt.packages(
    name="Install cron-apt and ruby",
    packages=["cron-apt", "ruby"],
    present=True,
)

# Copy configuration modification script
files.put(
    name="Copy cron-apt modification script",
    src="tasks/tmpl/etc/cron-apt/modify-cronapt.rb",
    dest="/etc/cron-apt/modify-cronapt.rb",
    mode="755",
)

# Get configuration from host data
cronapt_mailto = host.data.get("cronapt_mailto", "")

# Configure cron-apt
server.shell(
    name="Configure cron-apt",
    commands=[
        f"cd /etc/cron-apt && ruby modify-cronapt.rb config {cronapt_mailto} > config.tmp && mv config.tmp config"
    ],
)

# Cleanup modification script
files.file(
    name="Remove modification script",
    path="/etc/cron-apt/modify-cronapt.rb",
    present=False,
)