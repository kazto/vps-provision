# pyinfra inventory for VPS provisioning
# Target hosts for deployment

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Host data dictionary for reference
_host_data = {
    # Mail configuration - AWS SES
    "aws_ses_region": os.environ.get("AWS_SES_REGION"),
    "aws_ses_username": os.environ.get("AWS_SES_USERNAME"),
    "aws_ses_password": os.environ.get("AWS_SES_PASSWORD"),
    "host_name": os.environ.get("HOST_NAME"),
    "ses_relay_host": os.environ.get("SES_RELAY_HOST"),
    "logwatch_mailto": os.environ.get("LOGWATCH_MAILTO"),
    "logwatch_mailfrom": os.environ.get("LOGWATCH_MAILFROM"),
    "cronapt_mailto": os.environ.get("CRONAPT_MAILTO"),
    
    # Mastodon configuration
    "mastodon_db_pass": os.environ.get("MASTODON_DB_PASS"),
    "mastodon_smtp_server": os.environ.get("MASTODON_SMTP_SERVER"),
    "mastodon_smtp_login": os.environ.get("MASTODON_SMTP_LOGIN"),
    "mastodon_smtp_password": os.environ.get("MASTODON_SMTP_PASSWORD"),
    "mastodon_s3_bucket": os.environ.get("MASTODON_S3_BUCKET"),
    "mastodon_aws_access_key_id": os.environ.get("MASTODON_AWS_ACCESS_KEY_ID"),
    "mastodon_aws_secret_access_key": os.environ.get("MASTODON_AWS_SECRET_ACCESS_KEY"),
    "mastodon_s3_alias_host": os.environ.get("MASTODON_S3_ALIAS_HOST"),
    "mastodon_s3_endpoint": os.environ.get("MASTODON_S3_ENDPOINT"),
}

# Main target host with data
vps_hosts = [("4eiz.c.time4vps.cloud", _host_data)]

# Group definitions for different deployment scenarios
mastodon_hosts = [("4eiz.c.time4vps.cloud", _host_data)]

# For backward compatibility
host_data = {
    "4eiz.c.time4vps.cloud": _host_data
}