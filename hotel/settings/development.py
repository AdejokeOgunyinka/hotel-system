import dj_database_url
from decouple import config
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES['default'] = dj_database_url.parse(config('DATABASE_URL'))
