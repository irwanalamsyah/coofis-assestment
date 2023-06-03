from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DATABASES = {"default": env.db("DATABASE_URL")}
CSRF_TRUSTED_ORIGINS=env.list("CSRF_TRUSTED_ORIGINS")