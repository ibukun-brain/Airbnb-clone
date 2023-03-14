import dj_database_url
from .base_settings import *
from airbnb.settings.local.mailhog_settings import *

SECRET_KEY = 'django-insecure-w$*sk^mkhnj#t0hr-\
!=yk7qb2gd1=wy@*_f_j4z2=9s3!h%p=a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES["default"] = dj_database_url.parse(
    f"sqlite:////{BASE_DIR.joinpath(BASE_DIR.name)}.db", conn_max_age=600,
)


INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_URL = '/assets/'

STATICFILES_DIRS = [
    BASE_DIR / 'assets/'
]

STATIC_ROOT = BASE_DIR / "static_root"


MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
