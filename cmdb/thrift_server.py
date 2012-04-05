'''
Created on 2012-4-2

@author: yezi
'''
import os 
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from webservice.thriftservice import ThriftServer

application = ThriftServer.ThriftServer('thriftServerThread')