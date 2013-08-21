from meddy_project.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'meddy',
        'USER': 'meddyuser',
        'PASSWORD': 'meddypass',
        'HOST': '',
        'PORT': '',
    }
}
