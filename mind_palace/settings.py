import os
from pathlib import Path

from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open('config.yml') as file:
    config = load(file, Loader=Loader)


BASE_DIR = Path(__file__).resolve().parent.parent

# Basic settings
DEBUG = config.get('debug', False)
SECRET_KEY = config.get('secretKey')
ALLOWED_HOSTS = config.get('allowedHosts')
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = config.get('allowedCorsOrigins')
AUTH_USER_MODEL = 'user.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'mptt',
    'django_filters',
    'djoser',

    'mind_palace.user',
    'mind_palace.palace',
    'mind_palace.node',
    'mind_palace.learning',
    'mind_palace.learning.statistics',
    'mind_palace.learning_session',
    # 'mind_palace.learning.config',
]

smtp_config = config.get('smtp')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = smtp_config.get('host')
EMAIL_PORT = smtp_config.get('port')
EMAIL_HOST_USER = smtp_config.get('user')
EMAIL_HOST_PASSWORD = smtp_config.get('password')
EMAIL_USE_TLS = smtp_config.get('useTLS')


# APPLICATION SETTING
USER_LEARNING_SESSION_EXPIRE = 30  # In minutes

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}


# Authentication related settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', ),
}
DOMAIN = config.get('frontendUrl')
SITE_NAME = config.get('siteName')
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'PASSWORD_RESET_CONFIRM_URL': 'auth/password/reset/{uid}/{token}',
    'ACTIVATION_URL': 'auth/user/activation/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user': 'mind_palace.user.serializers.UserSerializer',
        'current_user': 'mind_palace.user.serializers.UserSerializer',
        'user_create': 'mind_palace.user.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}

ROOT_URLCONF = 'mind_palace.urls'

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

WSGI_APPLICATION = 'mind_palace.wsgi.application'

postgres_config = config.get('postgres')
DATABASES = {
    'default': {
        'ENGINE': postgres_config.get('driver', 'django.db.backends.postgresql_psycopg2'),
        'NAME': postgres_config.get('name'),
        'USER': postgres_config.get('user'),
        'PASSWORD': postgres_config.get('password'),
        'HOST': postgres_config.get('host'),
        'PORT': postgres_config.get('port', 5432),
    }
}

# SQL request logging settings
# LOGGING = {
#     'version': 1,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     }
# }


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = Path(BASE_DIR, 'static')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Application settings

# in minutes
UPDATE_NODE_AFTER_MINUTES = config.get('app', {}).get('updateNodeViewsAfter', 30)
