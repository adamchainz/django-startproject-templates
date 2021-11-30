import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DEBUG = os.environ.get("DEBUG", "") == "1"


# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "{{ project_name }}.core",
]

ROOT_URLCONF = "{{ project_name }}.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
