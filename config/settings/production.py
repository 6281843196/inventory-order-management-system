"""
Production settings.
"""

from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    "*",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}