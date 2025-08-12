# pyinfra inventory for VPS provisioning
# Target hosts for deployment

# Main target host
vps_hosts = ["kazto.net"]

# Group definitions for different deployment scenarios
mastodon_hosts = ["kazto.net"]

# Host data - equivalent to Ansible vault variables
host_data = {
    "kazto.net": {
        # Mail configuration - AWS SES
        "aws_ses_region": "us-east-1",
        "aws_ses_username": "",
        "aws_ses_password": "",
        "host_name": "kazto.net",
        "ses_relay_host": "",
        "logwatch_mailto": "",
        "logwatch_mailfrom": "",
        "cronapt_mailto": "",
        
        # Mastodon configuration
        "mastodon_db_pass": "",
        "mastodon_smtp_server": "",
        "mastodon_smtp_login": "",
        "mastodon_smtp_password": "",
        "mastodon_s3_bucket": "",
        "mastodon_aws_access_key_id": "",
        "mastodon_aws_secret_access_key": "",
        "mastodon_s3_alias_host": "",
        "mastodon_s3_endpoint": "",
    }
}