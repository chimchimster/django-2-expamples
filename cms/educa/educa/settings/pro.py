from .base import *
DEBUG = False
ADMINS = (
    ('Antonio M', 'email@mydomain.com'),
)
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}