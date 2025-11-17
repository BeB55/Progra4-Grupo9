import os
import mercadopago
import dj_database_url 
from pathlib import Path
from decouple import config
from dotenv import load_dotenv
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")

ORS_API_KEY = os.getenv("ORS_API_KEY")

MERCADOPAGO_ACCESS_TOKEN = os.getenv("MERCADOPAGO_ACCESS_TOKEN")
MERCADOPAGO_PUBLIC_KEY = os.getenv("MERCADOPAGO_PUBLIC_KEY")

# Agrega credenciales
sdk = mercadopago.SDK("TEST_ACCESS_TOKEN")

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y4o+3-%*@a_h5vx!=q(m@!mm%f7mctbz6gt+@0=&@q1=!ak-jn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]
STATIC_ROOT = BASE_DIR / "staticfiles"

ORS_API_KEY = os.getenv('ORS_API_KEY')

# Application definition

AUTH_USER_MODEL = 'users.CustomUser'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "core",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    "rest_framework",
    'widget_tweaks',
    "users",
    "products",
    "cart",
    "scraping",
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ACCOUNT_LOGIN_METHOD = ["username*", "password*"] 
ACCOUNT_SIGNUP_FIELDS = ["username*", "email*", "password1*", "password2*"]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'elmercadito.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

WSGI_APPLICATION = 'elmercadito.wsgi.application'


SOCIALACCOUNT_PROVIDERS = {
     'google': {
        "APP": {
             "client_id": GOOGLE_OAUTH_CLIENT_ID,
             "secret": GOOGLE_OAUTH_CLIENT_SECRET,
     } ,   
         'SCOPE': ['profile','email'],
         'AUTH_PARAMS': {'access_type': 'online'},
     }
}

# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://tu_feria_en_casa_user:xPKpwbKAa4q3bgLD8Ew3MStUWR2f4zxY@dpg-d4d9rvshg0os73dfcrn0-a.oregon-postgres.render.com/tu_feria_en_casa',
        conn_max_age=600
    )
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# This setting informs Django of the URI path from which your static files will be served to users
# Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...
STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / "static"]

# This production code might break development mode, 
# so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` 
    # (this is specific to Render)
    STATIC_ROOT = BASE_DIR / "staticfiles"

    # Enable the WhiteNoise storage backend, 
    # which compresses static files to reduce disk use
    # and renames the files with unique names for each version 
    # to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' 
