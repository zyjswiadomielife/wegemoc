"""
Django settings for wegemoc project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8*nylia8)^qbwa%5%@m(nt1lxoblv6@4s*+__u94t(rm48f!ge'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['wegemoc.pl']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'gdpr_assist',
    'stream_django',
    'likes',
    'questions',
    'comments',
    'sorl.thumbnail',
    'initial_avatars',
    'crispy_forms',
    'rest_framework',
    'pinax.messages',
    'dal',
    'dal_select2',
    'corsheaders',
    'tagulous',
    'tinymce',
    'autoslug',
    'accounts',
    'recipes',
    'bookmarks',
    'mptt',
    'home',
    'blog',
]

STREAM_API_KEY = 'uqgz6c8za6ve'
STREAM_API_SECRET = '356t477hunrphgy9b37ef5z9m4j5zca3cdmkbyukx7wbwjkwzthfnk55edyyhd5g'

#Tagulous
SERIALIZATION_MODULES = {
    'xml':    'tagulous.serializers.xml_serializer',
    'json':   'tagulous.serializers.json',
    'python': 'tagulous.serializers.python',
    'yaml':   'tagulous.serializers.pyyaml',
}

ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = '/recipes/feed/'
SITE_ID = 1

IFRAMELYKEY = '493c9ebbdfcbdac2a10d6b'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/account/%s" % u.username,
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    "http://wege.local:8000",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wegemoc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'pinax.messages.context_processors.user_messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

CSRF_COOKIE_NAME = "XSRF-TOKEN"

WSGI_APPLICATION = 'wegemoc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import dj_database_url

if DEBUG:
    DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gonano',
            'USER': os.environ.get('DATA_DB_USER'),
            'PASSWORD': os.environ.get('DATA_DB_PASS'),
            'HOST': os.environ.get('DATA_DB_HOST'),
            'PORT': '',
        },
        'gdpr_log': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'gdpr-log.sqlite3'),
        }
    }


else:
        DATABASES = {
            'default': dj_database_url.parse('postgres://postgres:035561540e5def53f159939bf27f07d7@dokku-postgres-wegemocdb:5432/wegemocdb'),
            'gdpr_log': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'gdpr-log.sqlite3'),
            }
        }

        DATABASE_ROUTERS = ['gdpr_assist.routers.EventLogRouter']

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = '/storage'
MEDIA_URL = '/media/'

#Sentry
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://49083fbfff2c4d48a3c4b50541cff4c6@o350874.ingest.sentry.io/5375488",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)