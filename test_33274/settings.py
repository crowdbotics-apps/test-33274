import os
import io
import environ
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env_file = os.path.join(BASE_DIR, ".env")
env = environ.Env()
env.read_env(env_file)

DEBUG = env.bool("DEBUG", default=False)

SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = env.list("HOST")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_REDIRECT", default=False)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'storages',
    'home',
    'widget_tweaks',
]

SITE_ID = 11

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',

]

ROOT_URLCONF = "test_33274.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'home/templates'),os.path.join(BASE_DIR, 'account/templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "test_33274.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


if env.str("DATABASE_URL", default=None):
    DATABASES = {"default": env.db()}


SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email','public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'first_name',
            'last_name',
            'middle name',
            'name',
            'name_format',
            'short_name',
            'gender',
        ],
 
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    },

    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],

        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ACCOUNT_ALLOW_REGISTRATION = env.bool("ACCOUNT_ALLOW_REGISTRATION", True)
SOCIALACCOUNT_ALLOW_REGISTRATION = env.bool("SOCIALACCOUNT_ALLOW_REGISTRATION", True)



# allauth / users
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# REST_AUTH_SERIALIZERS = {
#     # Replace password reset serializer to fix 500 error
#     "PASSWORD_RESET_SERIALIZER": "home.api.v1.serializers.PasswordSerializer",
# }
# REST_AUTH_REGISTER_SERIALIZERS = {
#     # Use custom serializer that has no username and matches web signup
#     "REGISTER_SERIALIZER": "home.api.v1.serializers.SignupSerializer",
# }

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY') 

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # value of your apikey
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
FROM_EMAIL = os.getenv("FROM_EMAIL")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AWS S3 config
# AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", "")
# AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", "")
# AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", "")
# AWS_STORAGE_REGION = env.str("AWS_STORAGE_REGION", "")

# USE_S3 = (
#     AWS_ACCESS_KEY_ID
#     and AWS_SECRET_ACCESS_KEY
#     and AWS_STORAGE_BUCKET_NAME
#     and AWS_STORAGE_REGION
# )

# if USE_S3:
#     AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", "")
#     AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
#     AWS_DEFAULT_ACL = env.str("AWS_DEFAULT_ACL", "public-read")
#     AWS_MEDIA_LOCATION = env.str("AWS_MEDIA_LOCATION", "media")
#     AWS_AUTO_CREATE_BUCKET = env.bool("AWS_AUTO_CREATE_BUCKET", True)
#     DEFAULT_FILE_STORAGE = env.str(
#         "DEFAULT_FILE_STORAGE", "home.storage_backends.MediaStorage"
#     )
#     MEDIA_URL = "/mediafiles/"
#     MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

# # Swagger settings for api docs
# SWAGGER_SETTINGS = {
#     "DEFAULT_INFO": f"{ROOT_URLCONF}.api_info",
# }

# # if DEBUG: #or not (EMAIL_HOST_USER and EMAIL_HOST_PASSWORD)
# #     # output email to console instead of sending
# #     if not DEBUG:
# #         logging.warning(
# #             "You should setup `SENDGRID_USERNAME` and `SENDGRID_PASSWORD` env vars to send emails."
# #         )
# #     EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# # GCP config
# GS_BUCKET_NAME = env.str("GS_BUCKET_NAME", "")
# if GS_BUCKET_NAME:
#     DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
#     STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
#     GS_DEFAULT_ACL = "publicRead"
