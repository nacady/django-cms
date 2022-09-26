try:
    import django
except ModuleNotFoundError:
    django = None

__version__ = '3.11.0'

if django and django.VERSION < (3, 2):
    default_app_config = 'cms.apps.CMSConfig'
