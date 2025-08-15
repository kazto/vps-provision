"""Test that base packages from base.py are installed"""

import testinfra


def test_base_packages_installed(host):
    """Test that base packages from base.py are installed"""
    base_packages = [
        "curl", "git", "vim", "tmux", "zsh", "build-essential",
        "libssl-dev", "libreadline-dev", "zlib1g-dev", "libncurses-dev",
        "libffi-dev", "libgdbm-dev", "libdb-dev", "libbz2-dev", "liblzma-dev",
        "libsqlite3-dev", "libxml2-dev", "libxslt1-dev", "libyaml-dev"
    ]
    
    for package in base_packages:
        assert host.package(package).is_installed, f"Base package {package} should be installed"