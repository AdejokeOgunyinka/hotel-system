from decouple import config


if config('ENVIRONMENT') == 'production':
   from .production import *
else:
   from .development import *
