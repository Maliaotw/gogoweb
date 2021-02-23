from .base import *  # noqa

import os

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

# GENERAL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get("MYSQL_HOST"),
        'NAME': os.environ.get("MYSQL_DATABASE"),
        'PORT': os.environ.get("MYSQL_PORT"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'TEST': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'test',
        },
    }
}
