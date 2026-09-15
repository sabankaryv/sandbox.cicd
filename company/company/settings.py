
from pathlib import Path
import json
import os


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# LOAD CONFIGURATION
# ============================================================

if os.path.exists(BASE_DIR / "settingsenv.json"):

    with open(BASE_DIR / "settingsenv.json") as f:
        config = json.load(f)
    #db_config = config["DB"]

else:

    config = {}

    db_config = {
        "DB_HOST": os.getenv("DB_HOST"),
        "DB_PORT": os.getenv("DB_PORT"),
        "DB_NAME": os.getenv("DB_NAME"),
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD"),
    }


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = 'django-insecure-5it23y$7+me#0zq3x##xcq&a_eh^17#01h28x@5uhux*_c@n-%'

DEBUG = True

ALLOWED_HOSTS = ["*"]


# ============================================================
# APPLICATION DEFINITION
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'employee',
    'department',
    "image_upload",
    "image_upload_production"
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================================
# URL / WSGI
# ============================================================

ROOT_URLCONF = 'company.urls'

WSGI_APPLICATION = 'company.wsgi.application'


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ============================================================
# DATABASE
# ============================================================

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",

#         "NAME": db_config["DB_NAME"],
#         "USER": db_config["DB_USER"],
#         "PASSWORD": db_config["DB_PASSWORD"],
#         "HOST": db_config["DB_HOST"],
#         "PORT": db_config["DB_PORT"],
#     }
# }


# ============================================================
# AWS CONFIGURATION
# ============================================================

AWS_ACCESS_KEY_ID = config.get(
    "AWS_ACCESS_KEY_ID",
    os.getenv("AWS_ACCESS_KEY_ID")
)

AWS_SECRET_ACCESS_KEY = config.get(
    "AWS_SECRET_ACCESS_KEY",
    os.getenv("AWS_SECRET_ACCESS_KEY")
)

AWS_REGION = config.get(
    "AWS_REGION",
    os.getenv("AWS_REGION")
)

AWS_S3_BUCKET_NAME = config.get(
    "AWS_S3_BUCKET_NAME",
    os.getenv("AWS_S3_BUCKET_NAME")
)


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = 'static/'
