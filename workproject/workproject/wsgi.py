"""
WSGI config for workproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../workproject')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workproject.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
