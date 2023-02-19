from .base import *  # noqa

ROOT_URLCONF = "demo.urls.frontend"

ALLOWED_HOSTS = ["quant-candles.com"]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

INSTALLED_APPS = [
    "semantic_admin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # PostgreSQL
    "django.contrib.postgres",
    # 3rd party
    "polymorphic",
    "rest_framework",
    "whitenoise",
    # Main
    "quant_candles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Whitenoise for static
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # For internationalization
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
