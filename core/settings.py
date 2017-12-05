"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, dj_database_url, socket

DATABASE_URL = os.environ.get('DATABASE_URL')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mp+hg4qrs6kc6k3^&cvnrg5*irggffprvdqcck&qe0af2&9jld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if(socket.gethostname() == 'debu-xubuntu' or DATABASE_URL) else False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'main_app',
    'dashboard',
    'fb_scrapper',
    
    #comment
    'django.contrib.sites',
    'django_comments',
    
]

# comment
SITE_ID = 10

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'core.urls'

CUSTOM_TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [CUSTOM_TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                
                'main_app.homepage_context_processors.header',
                
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL)
        }
else:
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'deshimemedb',
            'USER': 'werconcitus',
            'HOST': '127.0.0.1',
            'PORT': 5432,
            'PASSWORD': 'dmconcitus666',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# login
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/dashboard/'

# social auth
AUTHENTICATION_BACKENDS = (
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_ERROR_URL = LOGIN_URL
SOCIAL_AUTH_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# fb
# 9moja app
# SOCIAL_AUTH_FACEBOOK_KEY = '1659905954049233'  # App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = 'f33c1cdc6c24f53587bb4466e1d17896'  # App Secret
#testing
SOCIAL_AUTH_FACEBOOK_KEY = '361495860961861'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'a9255cff275001c025d19f69924eef6e'  # App Secret
SOCIAL_AUTH_TWITTER_KEY = 'dULiZCPsWc5u2OA086itWw2M2'  # App ID
SOCIAL_AUTH_TWITTER_SECRET = 'Yr9xXLlda9NfaPKA4ghCqmD9ZyybcDSlMiNz55CFmrgo8IfGYb'  # App Secret

# for dokku
if DATABASE_URL:
    SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('DOKKU_FB_APP_ID')
    SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('DOKKU_FB_APP_SECRET')
    SOCIAL_AUTH_TWITTER_KEY = os.environ.get('DOKKU_TW_APP_ID')
    SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('DOKKU_TW_APP_SECRET')