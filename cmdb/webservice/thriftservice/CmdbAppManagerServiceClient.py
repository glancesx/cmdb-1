'''
Created on 2012-3-26

@author: yezi
'''
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
import CmdbAppManagerService
import ttypes

class Client(object):
    '''
    classdocs
    '''
    def __init__(self,host,port):
        '''
        Constructor
        '''
        self.socket = TSocket.TSocket(host, port)
        self.transport = TTransport.TBufferedTransport(self.socket)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        
        
    def clientTest(self,cmdbQueryBoList):
        client = CmdbAppManagerService.Client(self.protocol)
        self.transport.open()
        result = client.getCmdbAppInfo(cmdbQueryBoList)
        print result[0].host_name
        self.transport.close()  
        
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9090
    cmdbQueryBo = ttypes.CmdbQueryBO()
    cmdbQueryBo.ip = '125.168.120.11'
    cmdbQueryBoList = []
    cmdbQueryBoList.append(cmdbQueryBo)
    
    Client(host,port).clientTest(cmdbQueryBoList)
    
    