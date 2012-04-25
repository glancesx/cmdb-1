'''
Created on 2012-2-27

@author: zi.yez
'''
from dal.models import CMDB_AppServer
from AppInstanceManager import AppInstanceManager
from django.db.models import Q


class AppServerManager(object):
    '''
    classdocs
    '''
    def __init__(self):
        pass
    
    def getAppServerInfoByCondition(self,conditionDict):
        condition = Q(flag = True)
        
        if conditionDict.has_key('id') and conditionDict['id'] is not None:
            condition.add(Q(id = conditionDict['id']), Q.AND)
        if conditionDict.has_key('host_name') and conditionDict['host_name'] is not None:
            condition.add(Q(host_name__icontains = conditionDict['host_name']), Q.AND)
        if conditionDict.has_key('cpu_core') and conditionDict['cpu_core'] is not None:
            condition.add(Q(cpu_core__icontains = conditionDict['cpu_core']), Q.AND)
        if conditionDict.has_key('cpu_type') and conditionDict['cpu_type'] is not None:
            condition.add(Q(cpu_type = conditionDict['cpu_type']), Q.AND)
        if conditionDict.has_key('memory') and conditionDict['memory'] is not None:
            condition.add(Q(memory = conditionDict['memory']), Q.AND)
        if conditionDict.has_key('sn') and conditionDict['sn'] is not None:
            condition.add(Q(sn__icontains = conditionDict['sn']), Q.AND)
        if conditionDict.has_key('startTime') and conditionDict['startTime'] is not None:
            condition.add(Q(gmtcreated__gte = conditionDict['startTime']), Q.AND)
        if conditionDict.has_key('endTime') and conditionDict['endTime'] is not None:
            condition.add(Q(gmtcreated__lte = conditionDict['endTime']), Q.AND)
            
        return CMDB_AppServer.objects.filter(condition)
    
    def insertAppServerInfo(self,appServerInfo):
        if appServerInfo.checkHostNameUnique(appServerInfo.host_name):
            #add logging
            pass            
        else:
            #add logging
            appServerInfo.flag = True
            appServerInfo.save()
    
    def updateAppServerInfo(self,appServerInfo):
        if not appServerInfo.checkCpuType(appServerInfo.cpu_type):
            #add logging
            return
        try:
            existAppServer = CMDB_AppServer.objects.get(id = appServerInfo.id,flag = True)
            existAppServer = appServerInfo
            existAppServer.gmtModifier = 'system'
            existAppServer.save()
        except:
            #add logging
            pass
        
    def deleteAppServerInfo(self,appServerId):
        try:
            existAppServer = CMDB_AppServer.objects.get(id = appServerId,flag = True)
            # false the appinstance
            AppInstanceManager().deleteAppInstanceInfoByAppServerId(appServerId)
            # false other source
                        
            existAppServer.flag = False
            existAppServer.gmtModifier = 'system'
            existAppServer.save()
        except:
            #add logging
            pass