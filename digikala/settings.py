from pathlib import Path
import os

import environ


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
)

environ.Env.read_env(BASE_DIR / ".env")


if os.getenv("__DJANGO_BUILDASSETS") == "true":
    SECRET_KEY = env(
        "SECRET_KEY",
        default="build-only-key-not-used-by-the-running-application",
    )
else:
    SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=[],
)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    "shop",
    "cart",
    "payment",
    "django.contrib.humanize",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "digikala.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "digikala.wsgi.application"


# فعلاً دیتابیس محلی است؛ در مرحله PostgreSQL تغییر می‌کند.
if os.getenv("__DJANGO_BUILDASSETS") == "true":
    # فقط برای collectstatic خود Liara در مرحله build
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "build.sqlite3",
        }
    }
else:
    # اجرای واقعی برنامه: PostgreSQL لیارا
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("POSTGRESQL_DB_NAME"),
            "USER": env("POSTGRESQL_DB_USER"),
            "PASSWORD": env("POSTGRESQL_DB_PASS"),
            "HOST": env("POSTGRESQL_DB_HOST"),
            "PORT": env("POSTGRESQL_DB_PORT"),
            "CONN_MAX_AGE": 600,
            "CONN_HEALTH_CHECKS": True,
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True


# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"


# Liara Object Storage / S3
AWS_ACCESS_KEY_ID = env("LIARA_ACCESS_KEY", default="")
AWS_SECRET_ACCESS_KEY = env("LIARA_SECRET_KEY", default="")
AWS_STORAGE_BUCKET_NAME = env("LIARA_BUCKET_NAME", default="")
AWS_S3_ENDPOINT_URL = env("LIARA_ENDPOINT_URL", default="")
AWS_S3_REGION_NAME = None

AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False

# آدرس عمومی فایل‌ها
AWS_S3_CUSTOM_DOMAIN = env(
    "LIARA_MEDIA_DOMAIN",
    default="",
)

MEDIA_URL = (
    f"https://{AWS_S3_CUSTOM_DOMAIN}/"
    if AWS_S3_CUSTOM_DOMAIN
    else "/media/"
)

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# این‌ها در Liara با مقدار True فعال می‌شوند.
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=False)
SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=False)
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=False)


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"