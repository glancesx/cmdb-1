'''
Created on 2012-3-30

@author: yezi
'''
import os 
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()