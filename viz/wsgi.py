"""
WSGI config for viz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viz.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root='viz/eventtia/static/eventtia')
application.add_files('viz/eventtia/static/eventtia', prefix='static/')