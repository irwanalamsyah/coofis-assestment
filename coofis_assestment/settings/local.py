from .base import *
from .base import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {"default": env.db("DATABASE_URL")}

