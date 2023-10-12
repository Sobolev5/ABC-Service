import os
import sys
from django.contrib.messages import constants as message_constants

from dotenv import load_dotenv
load_dotenv()

# COMMON
HOST = os.getenv("HOST")
HOST_PRETTY = os.getenv("HOST_PRETTY")
HOST_LANGUAGE = os.getenv("HOST_LANGUAGE", "en")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True # os.getenv("DEBUG") == "1"
PRODUCTION = os.getenv("PRODUCTION") == "1"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")

sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

# DATABASE
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# BROKER
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
AMQP_URI = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/vhost"


INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "debug_toolbar",
    "api",
    "api_drf",
    "education",
    "lesson7",
    "main",
    "chat",
    "user_profile",
)


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",    
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "site_middleware.GetUserData",
]


if DEBUG:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]


ALLOWED_HOSTS = [HOST]
CSRF_TRUSTED_ORIGINS = [f"http://{HOST}:1234"]


ROOT_URLCONF = "urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.csrf",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "context_processors.common",
            ],
        },
    },
]


WSGI_APPLICATION = "wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
        "PASSWORD": POSTGRES_PASSWORD,
    }
}

MESSAGE_TAGS = {
    message_constants.DEBUG: "debug",
    message_constants.INFO: "info",
    message_constants.SUCCESS: "success",
    message_constants.WARNING: "warning",
    message_constants.ERROR: "danger",
}


# LOCALIZATION
AVAILABLE_LANGUAGES = [HOST_LANGUAGE]
LANGUAGE_CODE = HOST_LANGUAGE
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


