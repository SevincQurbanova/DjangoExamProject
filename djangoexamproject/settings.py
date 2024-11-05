from datetime import timedelta
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG=True
SECRET_KEY = 'your-secret-key123654' 

AUTH_USER_MODEL = 'app.User'

AUTHENTICATION_BACKENDS = [
    'app.backends.CaseInsensitiveModelBackend',  # Replace 'yourapp' with your actual app name
    'django.contrib.auth.backends.ModelBackend',  # Default backend, keep this for fallback
]

# Celery configuration
CELERY_BROKER_URL = 'redis://djangoexam_redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://djangoexam_redis:6379/0'

# Set the default language
LANGUAGE_CODE = 'en'  # Default language code, e.g., 'en' for English, 'fr' for French

# Enable internationalization
USE_I18N = True

# Define the available languages
LANGUAGES = [
    ('en', 'English'),
    ('az', 'Azərbaycanca'),  # Add other languages you need
    # ('es', 'Spanish'),
    # ('de', 'German'),
]

# Specify the directory where translation files will be stored
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


STATIC_URL = '/static/'
ROOT_URLCONF = 'djangoexamproject.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoexamdb',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',  # Use localhost to connect from Django running locally
        'PORT': '5433',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'app',
    'drf_yasg',
    'django_celery_beat',
]

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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.BlockIPMiddleware',  # Add your custom middleware here
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),  # Access token expires in 1 week
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7), # Refresh token expires in 1 week
}


# Configure SWAGGER_SETTINGS for drf_yasg
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header using the Bearer scheme. Example: "Bearer {your JWT token}"',
        }
    },
    'USE_SESSION_AUTH': False,  # Ensures the Swagger UI does not prompt for Django's session login
    'JSON_EDITOR': True,        # Enables JSON editor in Swagger UI for complex data structures
    'REFETCH_SCHEMA_WITH_AUTH': True,  # Ensures schema is refetched with authorization headers applied
    'DEFAULT_MODEL_RENDERING': 'example',  # Shows example values for models by default
}