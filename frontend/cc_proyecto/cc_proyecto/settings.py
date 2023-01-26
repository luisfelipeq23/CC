"""
Django settings for cc_proyecto project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'srq@glu@+b)2yo5cj69q)w&94vt$27#(!rno*nudq(f+@gob+6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'cc_postgres', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'cc_proyecto',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django-keycloak-auth.middleware.KeycloakMiddleware',
]
#
# Exempt URIS

# # For example: ['core/banks', 'swagger']
KEYCLOAK_EXEMPT_URIS = []
KEYCLOAK_CONFIG = {
    'KEYCLOAK_SERVER_URL': 'localhost:8080/admin/master/console/',
    'KEYCLOAK_REALM': 'cc_realm',
    'KEYCLOAK_CLIENT_ID': 'cc_proyecto_cliente',
    'KEYCLOAK_CLIENT_SECRET_KEY': 'KCHMyvEgTsktOQFdmT1win8xfGMK0jdO'
}


# import keycloak
# from keycloak import KeycloakOpenID

# KEYCLOAK_SERVER = "localhost:8080/admin/master/console/"
# KEYCLOAK_REALM = "cc_realm"
# KEYCLOAK_CLIENT_ID = "cc_proyecto_cliente"
# KEYCLOAK_CLIENT_SECRET = "pEdyRFUneCZjYqoBH2tQV4F81jlhesnv"
# KEYCLOAK_REDIRECT_URL = "localhost:8000/download_repo/"

# # initialize the keycloak client
# keycloak_client = KeycloakOpenID(server_url=KEYCLOAK_SERVER,
#                                  realm_name=KEYCLOAK_REALM,
#                                  client_id=KEYCLOAK_CLIENT_ID,
#                                  client_secret=KEYCLOAK_CLIENT_SECRET
#                                 )

# # add the keycloak authentication backend
# AUTHENTICATION_BACKENDS = ["keycloak.backends.KeycloakBackend"]

# # configure the keycloak client for the application
# KEYCLOAK_OIDC_CLIENT = keycloak_client
# KEYCLOAK_OIDC_URL = KEYCLOAK_SERVER

ROOT_URLCONF = 'cc_proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'cc_app/templates'),],
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

WSGI_APPLICATION = 'cc_proyecto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "cc_cloud_db",
        'USER': "cc_cloud_user",
        'PASSWORD': "cc_cl0ud_p455",
        'HOST': 'cc_frontend_db',
        'PORT': '5432',
    }
}#172.18.0.2

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
