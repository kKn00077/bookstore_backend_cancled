from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', "*"]

# sqlite 환경
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
"""

# mysql 환경

SILENCED_SYSTEM_CHECKS = ['mysql.W003']

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cat_bookstore_local',
        'USER': 'root',
        'PASSWORD': 'test1234',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}