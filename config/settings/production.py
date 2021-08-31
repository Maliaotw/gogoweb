from .base import *  # noqa

import io
import os
import google.auth
from google.cloud import secretmanager

# Attempt to load the Project ID into the environment, safely failing on error.
try:
    _, os.environ["GOOGLE_CLOUD_PROJECT"] = google.auth.default()
except google.auth.exceptions.DefaultCredentialsError:
    pass

# [END_EXCLUDE]
if os.environ.get("GOOGLE_CLOUD_PROJECT", None):
    # Pull secrets from Secret Manager
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    client = secretmanager.SecretManagerServiceClient()
    settings_name = os.environ.get("SETTINGS_NAME", "gogoweb_settings")
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")
    env.read_env(io.StringIO(payload))


DJANGO_SUPERUSER_USERNAME = env("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_PASSWORD = env("DJANGO_SUPERUSER_PASSWORD")


# GENERAL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]


# MIDDLEWARE
MIDDLEWARE.append('django.middleware.security.SecurityMiddleware')
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')


# Database
# [START cloudrun_django_database_config]
# Use django-environ to parse the connection string
# DATABASES = {"default": env.db()}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get("MYSQL_HOST"),
        'NAME': os.environ.get("MYSQL_DATABASE"),
        'PORT': os.environ.get("MYSQL_PORT"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
    }
}


# If the flag as been set, configure to use proxy
if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
    DATABASES["default"]["HOST"] = "127.0.0.1"
    DATABASES["default"]["PORT"] = "3306"
    DATABASES["default"]["NAME"] = "gogoweb"

# [END cloudrun_django_database_config]
