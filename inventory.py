# pyinfra inventory for VPS provisioning
# Target hosts for deployment

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Main target host
vps_hosts = ["4eiz.c.time4vps.cloud"]

# Group definitions for different deployment scenarios
mastodon_hosts = ["4eiz.c.time4vps.cloud"]

# Host data - equivalent to Ansible vault variables
host_data = {
    "4eiz.c.time4vps.cloud": {
        # Mail configuration - AWS SES
        "aws_ses_region": os.getenv("AWS_SES_REGION", "ap-northeast-1"),
        "aws_ses_username": os.getenv("AWS_SES_USERNAME", ""),
        "aws_ses_password": os.getenv("AWS_SES_PASSWORD", ""),
        "host_name": os.getenv("HOST_NAME", "kazto.net"),
        "ses_relay_host": os.getenv("SES_RELAY_HOST", ""),
        "logwatch_mailto": os.getenv("LOGWATCH_MAILTO", ""),
        "logwatch_mailfrom": os.getenv("LOGWATCH_MAILFROM", ""),
        "cronapt_mailto": os.getenv("CRONAPT_MAILTO", ""),
        
        # Mastodon configuration
        "mastodon_db_pass": os.getenv("MASTODON_DB_PASS", ""),
        "mastodon_smtp_server": os.getenv("MASTODON_SMTP_SERVER", ""),
        "mastodon_smtp_login": os.getenv("MASTODON_SMTP_LOGIN", ""),
        "mastodon_smtp_password": os.getenv("MASTODON_SMTP_PASSWORD", ""),
        "mastodon_s3_bucket": os.getenv("MASTODON_S3_BUCKET", ""),
        "mastodon_aws_access_key_id": os.getenv("MASTODON_AWS_ACCESS_KEY_ID", ""),
        "mastodon_aws_secret_access_key": os.getenv("MASTODON_AWS_SECRET_ACCESS_KEY", ""),
        "mastodon_s3_alias_host": os.getenv("MASTODON_S3_ALIAS_HOST", ""),
        "mastodon_s3_endpoint": os.getenv("MASTODON_S3_ENDPOINT", ""),
    }
}