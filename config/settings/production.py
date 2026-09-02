"""
Production settings.
"""

from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    "inventory-order-management-system-jq42.onrender.com",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}