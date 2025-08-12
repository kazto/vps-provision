"""
Docker installation and configuration
Equivalent to ansible role-common/tasks/docker.yml
"""

from pyinfra.operations import apt, systemd

# Install Docker
apt.packages(
    name="Install Docker",
    packages=["docker.io"],
    present=True,
)

# Enable and start Docker service
systemd.service(
    name="Enable and start Docker service",
    service="docker",
    enabled=True,
    running=True,
)