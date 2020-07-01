import os

from django.core.exceptions import ImproperlyConfigured
from response.slack.client import SlackClient

def get_env_var(setting, warn_only=False):
    value = os.getenv(setting, None)

    if not value:
        error_msg = f"ImproperlyConfigured: Set {setting} environment variable"
        if warn_only:
            logger.warn(error_msg)
        else:
            raise ImproperlyConfigured(error_msg)
    else:
        value = value.replace('"', "")  # remove start/end quotes

    return value

if get_env_var("DJANGO_ENV") == "prod":
    with open('/vault/secrets/slack-token', 'r') as f:
        SLACK_TOKEN = f.read().rstrip('\n')
else:
    SLACK_TOKEN = get_env_var("SLACK_TOKEN")
SLACK_CLIENT = SlackClient(SLACK_TOKEN)

