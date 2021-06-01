from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: 추후에 변경
ALLOWED_HOSTS = ['Catbookstoredev-env.eba-2kspmfxk.ap-northeast-2.elasticbeanstalk.com', '127.0.0.1', "*"]

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