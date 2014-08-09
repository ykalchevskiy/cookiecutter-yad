"""
Django settings for {{ cookiecutter.project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

Security: https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
Database: https://docs.djangoproject.com/en/dev/ref/settings/#databases
Internationalization: https://docs.djangoproject.com/en/dev/topics/i18n/
Static: https://docs.djangoproject.com/en/dev/howto/static-files/
"""

import os

from django.conf import global_settings  # noqa
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse_lazy  # noqa


def get_env_variable(var_name):
    """Get the environment variable or return an exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {var_name} environment variable".format(
            var_name=var_name
        )
    raise ImproperlyConfigured(error_msg)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
REPO_DIR = os.path.dirname(BASE_DIR)

SECRET_KEY = get_env_variable('SECRET_KEY')

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'apps.{{ cookiecutter.app_name }}',
)

THIRD_PARTY = ()

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'

WSGI_APPLICATION = '{{ cookiecutter.project_name }}.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.db'),
    }
}


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(REPO_DIR, 'assets')
STATIC_URL = '/static/'


# Third party

