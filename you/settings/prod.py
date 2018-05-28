import json

import dj_database_url

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = json.dumps(os.environ.get('ALLOWED_HOSTS'))

DATABASES = {
    'default': dj_database_url.config(os.environ.get('DATABASE_URL'))
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
