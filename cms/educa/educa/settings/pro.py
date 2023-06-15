from .base import *
DEBUG = False
ADMINS = (
    ('Artem K', 'email@mydomain.com'),
)
ALLOWED_HOSTS = ['.educaproject.com']
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

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True