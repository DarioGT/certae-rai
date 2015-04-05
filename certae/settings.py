# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

"""
Django settings for certae project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import site

# Build paths inside the project like this: os.path.join(PPATH, ...)
PPATH = os.path.dirname(os.path.dirname(__file__))


EXTJS_VERSION = '4.2.1'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')3)8tas^#g$3#)f-@owl-o*pi&b-ko0e$5kcggs2xl5t+uv#fq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'localhost', # Allow domain and subdomains
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'protobase',
    'protoLib',
    'prototype',
#   'rai02db',
    'rai01ref',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'certae.urls'

WSGI_APPLICATION = 'certae.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PPATH, 'db','testproto.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-ca'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PPATH, 'media/')
FILE_UPLOAD_PERMISSIONS = 0644

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

if PPATH.startswith('/'):
    EXT_PATH = '/opt/lib/ext-%(extjsversion)s' % {"extjsversion" : EXTJS_VERSION}
else:
    EXT_PATH = 'd:/data/ExtJs'

TEMPLATE_DIRS = (
    os.path.join(PPATH, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(PPATH, 'static'),
    os.path.join(site.USER_SITE, 'protobase/static'),
    EXT_PATH,
)

SITE_ID = 1
