"""
Django settings for briane_backend project.
"""

import os
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Seguridad ──────────────────────────────────────────────────────────────
SECRET_KEY = config('DJANGO_SECRET_KEY')

DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

# ── Aplicaciones ───────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party
    'rest_framework',
    'corsheaders',
    # Local apps
    'content',
    'services',
    'company',
    'forms_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # Servir estáticos en producción
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'briane_backend.urls'

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

WSGI_APPLICATION = 'briane_backend.wsgi.application'

# ── Base de datos ──────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     config('DB_NAME',     default='briane_db'),
        'USER':     config('DB_USER',     default='briane_user'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST':     config('DB_HOST',     default='localhost'),
        'PORT':     config('DB_PORT',     default='5432'),
        'CONN_MAX_AGE': 60,   # conexiones persistentes
    }
}

# ── Validación de contraseñas ──────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internacionalización ───────────────────────────────────────────────────
LANGUAGE_CODE = 'es'
TIME_ZONE     = 'America/Lima'
USE_I18N      = True
USE_TZ        = True

# ── Archivos estáticos ─────────────────────────────────────────────────────
STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ── Archivos multimedia (CVs, imágenes, etc.) ──────────────────────────────
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── CORS ───────────────────────────────────────────────────────────────────
_cors_origins = config('CORS_ALLOWED_ORIGINS', default='', cast=Csv())

if DEBUG:
    # En desarrollo: cualquier puerto de localhost
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r'^http://localhost:\d+$',
        r'^http://127\.0\.0\.1:\d+$',
    ]
else:
    CORS_ALLOWED_ORIGINS = _cors_origins

# ── DRF ────────────────────────────────────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
}

# ── Seguridad en producción ────────────────────────────────────────────────
USE_HTTPS = config('USE_HTTPS', default=False, cast=bool)

if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True   # siempre activo en producción

    # Activar solo cuando el servidor tenga SSL/TLS real configurado en Nginx
    if USE_HTTPS:
        SECURE_PROXY_SSL_HEADER       = ('HTTP_X_FORWARDED_PROTO', 'https')
        SECURE_SSL_REDIRECT           = True
        SESSION_COOKIE_SECURE         = True
        CSRF_COOKIE_SECURE            = True
        SECURE_HSTS_SECONDS           = 31536000   # 1 año
        SECURE_HSTS_INCLUDE_SUBDOMAINS = True
        SECURE_HSTS_PRELOAD           = True
