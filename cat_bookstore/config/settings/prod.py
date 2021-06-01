from .base import *
import os

ADMIN_ID = env('ADMIN_ID')
ADMIN_PW = env('ADMIN_PW')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: 추후에 변경
ALLOWED_HOSTS = ['cat-bookstore-api.eba-2kspmfxk.ap-northeast-2.elasticbeanstalk.com', "*"]

# TODO: 추후에 변경
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('RDS_DB_NAME', env('DB_NAME')),
        'USER': os.environ.get('RDS_USERNAME', env('DB_USERNAME')),
        'PASSWORD': os.environ.get('RDS_PASSWORD', env('DB_PASSWORD')),
        'HOST': os.environ.get('RDS_HOSTNAME', env('DB_HOST')),
        'PORT': os.environ.get('RDS_PORT', env('DB_PORT'))
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')