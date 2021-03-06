"""
Django settings for trade project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z(*t7=7-m*gf594nj#c(g#-0*$t1dzo@vxe(+6g7w)r48nraxp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'tinymce',
    'search',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user.middleware.LoginCheckMiddleware'
]

ROOT_URLCONF = 'trade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
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

WSGI_APPLICATION = 'trade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'trade_web',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     },
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trade_web',
        'USER': 'root',
        'PASSWORD': 'Shengshikeji@1',
        'HOST': 'rm-2vc5xhi77ulz46a8nuo.mysql.cn-chengdu.rds.aliyuncs.com',
        'PORT': '3306',
    },
    # 'newtrade': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'new_tradeinfo',
    #     'USER': 'root',
    #     'PASSWORD': 'Shengshikeji.1',
    #     'HOST': '47.98.164.255',
    #     'PORT': '3306',
    # },
    'beijingdb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ApiRecord',
        'USER': 'root',
        'PASSWORD': 'Shengshikeji@1',
        'HOST': 'rm-2vc5xhi77ulz46a8nuo.mysql.cn-chengdu.rds.aliyuncs.com',
        'PORT': '3306',
    },
    # 'oa_db': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'sstrade_pro',
    #     'USER': 'root',
    #     'PASSWORD': 'Shengshikeji.1',
    #     'HOST': '47.98.164.255',
    #     'PORT': '3306',
    # }
}


PRODUCT = 1
VERSION = '3.6'


SERVER_LIST = [
    "8.219.43.39:80",
    "47.88.79.176:80",
    "47.90.252.192:80",
    # "47.241.32.25:8080",# ??????????????????
    # "47.252.3.225:8080",# ???????????????1
    # "147.139.6.71:8080",# ???????????????
    # # "47.88.19.94:8080",# ???????????????2
    # "47.254.241.59:8080",# ????????????
]


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

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
# STATIC_ROOT = os.path.join(BASE_DIR,'static')
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = False  # ????????????TLS??????????????????(???????????????????????????????????????????????????????????????????????????)
EMAIL_USE_SSL = True  # ????????????SSL?????????qq????????????????????????
EMAIL_PORT = 465  # ????????????SMTP???????????????


# EMAIL_HOST_USER = '790187177@qq.com'  # ???????????????????????????
# EMAIL_HOST_PASSWORD = 'tdqecosbjrqjbbbe'



