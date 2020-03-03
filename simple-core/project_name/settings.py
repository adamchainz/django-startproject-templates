import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get("DEBUG", "") == "1"

SECRET_KEY = "{{ secret_key }}"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "{{ project_name }}.core",
]

ROOT_URLCONF = "{{ project_name }}.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}
