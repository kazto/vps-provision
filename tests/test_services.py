"""Test that all configured services are in expected state"""

import testinfra


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