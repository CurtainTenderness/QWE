"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.20.

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
SECRET_KEY = '3^el!^yyv$2*-)6v5%0tt7le471+7*6ma#rgr87_#3s5zaiztv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 让任意IP地址写都可以访问
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myblog',
    'tinymce',
    'haystack',
    'mysearch',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['temp'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'goods',
        'USER': 'root',
        'PASSWORD': '123456'
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# tinymce 的配置项
TINYMCE_JS_URL = "/static/tiny_mce/tiny_mce.js"
TINYMCE_JS_ROOT = "/static/tiny_mce/"
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'width': 600,
    'height': 400,
}

# redis缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 选中的数据库
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD":密码
        }
    }
}

# qq IMAP/SMTP 配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25  # 或者 465/587 是设置了 SSL 加密方式
# 发送邮件的邮箱
EMAIL_HOST_USER = '674608896@qq.com'
# 在邮箱中设置的客户端授权密码
# 如果重新设置了新的授权码,直接使用最新的授权码即可
EMAIL_HOST_PASSWORD = 'xxxxxxxxxx'
# 这里必须是 True，否则发送不成功
EMAIL_USE_TLS = True
# 收件人看到的发件人, 必须是一直且有效的
EMAIL_FROM = 'Tencent<674608896@qq.com>'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'mysearch.whoosh_cn_backend.WhooshEngine',  # 将来需要修改
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
