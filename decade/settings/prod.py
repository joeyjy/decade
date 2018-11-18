"""Development settings and globals."""

from os.path import join, normpath

from .base import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default':{
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
    }
}
