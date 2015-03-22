DJANGO_INSTALLED = False
DJANGO_CONFIGURED = False
DJANGO_SETTINGS = None

try:
    import django
    DJANGO_INSTALLED = True
except ImportError:
    pass

if DJANGO_INSTALLED:
    from django.core.exceptions import ImproperlyConfigured
    try:
        from django.conf import settings as DJANGO_SETTINGS
        DJANGO_SETTINGS.get('', None)
        DJANGO_CONFIGURED = True
    except ImproperlyConfigured:
        DJANGO_SETTINGS = None