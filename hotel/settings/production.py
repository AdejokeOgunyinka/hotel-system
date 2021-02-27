import dj_database_url
from decouple import config
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
