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

#start daemon thread for thrift server
from webservice import ThriftServer
import thread

thread.start_new_thread(ThriftServer.ThriftServer().start,())