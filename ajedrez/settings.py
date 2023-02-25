"""
Django settings for ajedrez project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import environ
import locale
from pathlib import Path

# Para que las fechas se muestren en español
# en pythonanywhere esto no funciona, para que funcione:
# locale.setlocalte(locale.LC_TIME, 'es_ES') solo para los entornos conda lo dejamos
# como esta aquí.
locale.setlocale(locale.LC_TIME, '')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-b-hv2c4(1j9!f3--c02zaeys#m0m+ni9hs4_+)ti1c-ujv8#ye'
SECRET_KEY = env('SECRET_KEY')

GOOGLE_RECAPTCHA_SITE_KEY = env('GOOGLE_RECAPTCHA_SITE_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = env('GOOGLE_RECAPTCHA_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configuracion del correo
EMAIL_HOST = 'smtp.zoho.eu'
EMAIL_HOST_USER = 'info@mbsocialweb.net'
EMAIL_HOST_PASSWORD = 'manjaro2018'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'circuitos.apps.CircuitosConfig',
    'core.apps.CoreConfig',
    'contacto.apps.ContactoConfig',
    'ckeditor',
    'ckeditor_uploader',
    'cronica.apps.CronicaConfig',
    'blog.apps.BlogConfig',
    'escuelas.apps.EscuelasConfig',
    'normativa.apps.NormativaConfig',
    'page.apps.PageConfig',
    'taggit',
]

CKEDITOR_UPLOAD_PATH = "uploads/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'ajedrez.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ajedrez.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'

# Media config
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':
            'full',
        'extraPlugins':
            ','.join([
                'image2',  # the upload image feature
                # your extra plugins here
                'div'
            ]),
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
