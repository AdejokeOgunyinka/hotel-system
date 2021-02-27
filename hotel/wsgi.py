"""
WSGI config for hotel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

environment = config('ENVIRONMENT')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'hotel.settings.{environment}')

application = get_wsgi_application()
