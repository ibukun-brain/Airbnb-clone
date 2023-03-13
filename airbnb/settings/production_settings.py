from base_settings import *
from airbnb.utils.env_variable import get_env_variable

SECRET_KEY = get_env_variable('SECRET_KEY', 'XXXX')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable('DEBUG', 'XXXX')

ALLOWED_HOSTS = ["*"]
