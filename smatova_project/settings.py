"""
Django settings for smatova_project project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r@o@43eq07e5$1!sn7hgqq#+8td6328ht1kv!na*p66i$09@6^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'social_django',
    'basis.apps.BasisConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smatova_project.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'smatova_project.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
"""
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tatsm.reg@gmail.com'
EMAIL_HOST_PASSWORD = 'TatSmReg2019*'
EMAIL_USE_TLS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend',

    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# login settings
LOGIN_URL = '/basis/login/'
LOGIN_REDIRECT_URL = '/basis/'  # после входа открывает начальную страницу

LOGOUT_URL = '/basis/logout/'
# LOGOUT_REDIRECT_URL = '/basis/'

SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.11'
SOCIAL_AUTH_FACEBOOK_KEY = '441169157621408'        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '9cdebda9761fe1aaeaf14e90acc8d1a2'  # App Secret

SOCIAL_AUTH_GITHUB_KEY = 'ffc7fc7c9f42ba9e7b77'        # App ID
SOCIAL_AUTH_GITHUB_SECRET = '8c69424db17b16e4c09371a2bc0d57d88bb0a190'  # App Secret

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '78pro9uxsyejr3'        # App ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'BuljHeHqC2QRihao'  # App Secret
