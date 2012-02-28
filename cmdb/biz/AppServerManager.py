'''
Created on 2012-2-27

@author: zi.yez
'''
from cmdb.dal.models import CMDB_AppServer

class AppServerManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
    
    def getAppServerInfo(self):
        return CMDB_AppServer.objects.filter(flag = True)
    
    def getAppServerInfoByHostName(self,hostName):
        if hostName is None:
            #add logging
            return
        return CMDB_AppServer.objects.filter(host_name__contains = hostName,flag = True)
    
    def getAppServerInfoByCPUCore(self,cpuCore):
        if cpuCore is None:
            #add logging
            return
        return CMDB_AppServer.objects.filter(cpu_core__contains = cpuCore,flag = True)
    
        