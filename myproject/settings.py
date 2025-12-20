import os
from pathlib import Path
from google.cloud import secretmanager_v1  # Correct import for Secret Manager

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key & debug
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-cloudrun-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

# Allowed hosts
ALLOWED_HOSTS = ['*']  # Production: replace with your domain

# ✅ CSRF Trusted Origins for Cloud Run
CSRF_TRUSTED_ORIGINS = [
    "https://django-app-918955775042.asia-south1.run.app"
]

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Your Django app
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Root URL config
ROOT_URLCONF = 'myproject.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

# WSGI
WSGI_APPLICATION = 'myproject.wsgi.application'

# 🔐 Secret Manager helper function
def get_secret(secret_name):
    project_id = os.environ.get("GCP_PROJECT")  # Cloud Run env variable
    client = secretmanager_v1.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

# 🟢 Database (Cloud SQL MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret("MYSQL_DB"),
        'USER': get_secret("MYSQL_USER"),
        'PASSWORD': get_secret("MYSQL_PASSWORD"),
        # Cloud SQL connection via private IP or Cloud SQL Auth proxy socket
        'HOST': get_secret("MYSQL_HOST"),  # e.g., /cloudsql/<INSTANCE_CONNECTION_NAME>
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

