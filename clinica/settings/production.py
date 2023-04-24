from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['clinicamodelomoron.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd71ldkiesmq10g',
        'USER': 'aadoqrvssifptx',
        'PASSWORD': '2c2c6d8100bcb760d19eeb5c664a09507e1a66dcd9418cb85718db98a666080b',
        'HOST': 'ec2-34-227-120-79.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')

