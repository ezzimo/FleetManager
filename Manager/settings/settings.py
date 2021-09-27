import os
import sys
from glob import glob
from pathlib import Path

import dj_database_url
import environ
from django.core.management.utils import get_random_secret_key

from .storage import BASE_DIR, STATIC_ROOT, STATIC_URL, STATICFILES_DIRS

# GDAL_LIBRARY_PATH = glob("/usr/lib/libgdal.so.*")[0]
# GEOS_LIBRARY_PATH = glob("/usr/lib/libgeos_c.so.*")[0]

env = environ.Env()
environ.Env.read_env()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS")
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account",
    "vehicle",
    "refuel",
    "django.contrib.gis",
    "storages",
]

MIDDLEWARE = [
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Manager.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "NAME": "manage",
            "USER": "testuser",
            "PASSWORD": "Lin123",
            "HOST": "localhost",
            "PORT": "",
        }
    }
elif len(sys.argv) > 0:
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Customized user model
AUTH_USER_MODEL = "account.User"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"
# Email settings
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Configure Django App for Heroku.
import django_heroku

GEOS_LIBRARY_PATH = os.getenv("GEOS_LIBRARY_PATH")
GDAL_LIBRARY_PATH = os.getenv("GDAL_LIBRARY_PATH")

django_heroku.settings(locals())
