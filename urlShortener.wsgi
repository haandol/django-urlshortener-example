import os
import sys

sys.path.append('/home/hg')

os.environ['DJANGO_SETTINGS_MODULE'] = 'urlShortener.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
