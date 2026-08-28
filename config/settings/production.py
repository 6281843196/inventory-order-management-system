"""
Production settings.
"""

from .base import *


DEBUG = False

ALLOWED_HOSTS = [
    # Add production domain here later
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}