'''
Created on 2012-2-27

@author: zi.yez
'''
from cmdb.dal.models import CMDB_AppServer,CMDB_Dictionary
from django.db.models import Q


class AppServerManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
    
    def getAppServerInfoByCondition(self,hostName,cpuCore,cpuType,serverMemory,serverSn,startTime,endTime):
        condition = Q(flag = True)
             
        if hostName is not None:
            condition.add(Q(host_name__icontains = hostName), Q.AND)
        if cpuCore is not None:
            condition.add(Q(cpu_core__icontains = cpuCore), Q.AND)
        if cpuType is not None:
            condition.add(Q(cpu_type = cpuType), Q.AND)
        if serverMemory is not None:
            condition.add(Q(memory = serverMemory), Q.AND)
        if serverSn is not None:
            condition.add(Q(sn__icontains = serverSn), Q.AND)
        if startTime is not None:
            condition.add(Q(gmtcreated__gte = startTime), Q.AND)
        if endTime is not None:
            condition.add(Q(gmtcreated__lte = endTime), Q.AND)
            
        return CMDB_AppServer.objects.filter(condition)
    
    def insertAppServerInfo(self,appServerList):
        appServerInfo = CMDB_AppServer()
        for appServerInfo in appServerList:
            if self.__checkHostNameUnique(appServerInfo.host_name):
                #add logging
                pass
            elif not self.__checkCpuType(appServerInfo.cpu_type):
                #add logging
                pass
            else:
                #add logging
                appServerInfo.flag = True
                appServerInfo.save()
    
    def updateAppServerInfo(self,appServerInfo):
        if not self.__checkCpuType(appServerInfo.cpu_type):
            #add logging
            return
        ExistAppServer = CMDB_AppServer.objects.filter(appServerInfo.id,flag = True)
        if ExistAppServer:
            ExistAppServer = appServerInfo
            ExistAppServer.gmtModifier = 'system'
            ExistAppServer.save()
        else:
            return            
    
    def __checkCpuType(self,cpuType):
        return CMDB_Dictionary.objects.filter(key = cpuType, key_type = 'CPU_TYPE')
        
    def __checkHostNameUnique(self,hostName):                
        return CMDB_AppServer.objects.filter(host_name__iexact = hostName,flag = True)            