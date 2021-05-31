from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: 추후에 변경
ALLOWED_HOSTS = ['127.0.0.1', "*"]

# TODO: 추후에 변경
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}