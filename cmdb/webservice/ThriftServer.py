'''
Created on 2012-3-23

@author: yezi
'''
from webservice.thriftservice import CmdbAppManagerService
from webservice.ServiceHandler import AppManagerServiceHandler
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from settings import THRIFTSERVICE
import logging

logger = logging.getLogger(__name__)

class ThriftServer(object):
    def __init__(self):
        self.port = THRIFTSERVICE['port']
        self.transport = TSocket.TServerSocket(self.port)
        self.tfactory = TTransport.TBufferedTransportFactory()
        self.pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    
    def start(self):
        if not self.__port_is_used(self.port):
            logger.info('The port %d is free,start to load handler %s' %(self.port,AppManagerServiceHandler().__class__.__name__))
            self.loadHandler(AppManagerServiceHandler())
    
    def loadHandler(self,handler):
        processor = CmdbAppManagerService.Processor(handler)
        server = TServer.TThreadPoolServer(processor,self.transport,self.tfactory,self.pfactory)
        print 'Starting the server...'
        server.serve()
        print 'done.'
        
    def __port_is_used(self,port):
        import socket
        TIME_OUT = 1
        HOST = '127.0.0.1'
    
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sk.settimeout(TIME_OUT)
        try:
            sk.bind((HOST,port))
            sk.close()
        except socket.error:
            return True
        return False