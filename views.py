import sys
from django import get_version
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings


def get_python_version():
    return sys.version


def get_database_engine():
    return settings.DATABASES['default']['ENGINE'].split('.')[-1]


def get_installed_apps():
    return settings.INSTALLED_APPS


def get_debug_mode():
    return settings.DEBUG


def get_template_debug_mode():
    return settings.TEMPLATE_DEBUG


def get_path(request):
    path = request.META.get('PATH', None)
    if path:
        return [p for p in path.split(":")]
    return None


def info(request):

    context = {
        'django_version':  get_version(),
        'database_engine': get_database_engine(),
        'python_version': get_python_version(),
        # settings
        'settings_debug_mode': get_debug_mode(),
        'settings_template_debug_mode': get_template_debug_mode(),
        'settings_installed_apps': get_installed_apps(),
        'paths': get_path(request),
    }

    return render_to_response('index.html', context,
                              context_instance=RequestContext(request))
