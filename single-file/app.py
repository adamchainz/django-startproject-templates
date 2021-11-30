import html
import os
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path

settings.configure(
    DEBUG=(os.environ.get("DEBUG", "") == "1"),
    # Dangerous: disable host header validation
    ALLOWED_HOSTS=["*"],
    # Make this module the urlconf
    ROOT_URLCONF=__name__,
)


def index(request):
    name = request.GET.get("name", "World")
    return HttpResponse(f"Hello, {html.escape(name)}!")


urlpatterns = [
    path("", index),
]

app = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
