#!/usr/bin/env python3
"""
Configuration management for VPS provisioning
Handles secrets and environment variables
"""

import os
from pathlib import Path

# Base configuration directory
CONFIG_DIR = Path(__file__).parent

def load_secrets():
    """
    Load secrets from environment variables or .env file
    Alternative to Ansible vault
    """
    secrets = {}
    
    # Try to load from .env file if it exists
    env_file = CONFIG_DIR / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    secrets[key] = value
    
    # Override with environment variables
    secret_keys = [
        "MAILGUN_ACCOUNT",
        "MAILGUN_API_KEY", 
        "HOST_NAME",
        "RELAY_HOST",
        "LOGWATCH_MAILTO",
        "LOGWATCH_MAILFROM",
        "CRONAPT_MAILTO",
        "MASTODON_DB_PASS",
        "MASTODON_SMTP_SERVER",
        "MASTODON_SMTP_LOGIN", 
        "MASTODON_SMTP_PASSWORD",
        "MASTODON_S3_BUCKET",
        "MASTODON_AWS_ACCESS_KEY_ID",
        "MASTODON_AWS_SECRET_ACCESS_KEY",
        "MASTODON_S3_ALIAS_HOST",
        "MASTODON_S3_ENDPOINT",
    ]
    
    for key in secret_keys:
        if key in os.environ:
            secrets[key] = os.environ[key]
    
    return secrets

def get_host_data():
    """
    Get host-specific configuration data
    """
    secrets = load_secrets()
    
    return {
        "kazto.net": {
            # Mail configuration
            "mailgun_account": secrets.get("MAILGUN_ACCOUNT", ""),
            "mailgun_api_key": secrets.get("MAILGUN_API_KEY", ""),
            "host_name": secrets.get("HOST_NAME", "kazto.net"),
            "relay_host": secrets.get("RELAY_HOST", ""), 
            "logwatch_mailto": secrets.get("LOGWATCH_MAILTO", ""),
            "logwatch_mailfrom": secrets.get("LOGWATCH_MAILFROM", ""),
            "cronapt_mailto": secrets.get("CRONAPT_MAILTO", ""),
            
            # Mastodon configuration
            "mastodon_db_pass": secrets.get("MASTODON_DB_PASS", ""),
            "mastodon_smtp_server": secrets.get("MASTODON_SMTP_SERVER", ""),
            "mastodon_smtp_login": secrets.get("MASTODON_SMTP_LOGIN", ""),
            "mastodon_smtp_password": secrets.get("MASTODON_SMTP_PASSWORD", ""),
            "mastodon_s3_bucket": secrets.get("MASTODON_S3_BUCKET", ""),
            "mastodon_aws_access_key_id": secrets.get("MASTODON_AWS_ACCESS_KEY_ID", ""),
            "mastodon_aws_secret_access_key": secrets.get("MASTODON_AWS_SECRET_ACCESS_KEY", ""),
            "mastodon_s3_alias_host": secrets.get("MASTODON_S3_ALIAS_HOST", ""),
            "mastodon_s3_endpoint": secrets.get("MASTODON_S3_ENDPOINT", ""),
        }
    }