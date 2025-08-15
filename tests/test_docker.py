"""Test that Docker from docker.py is installed and running"""

import testinfra


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