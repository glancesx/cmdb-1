'''
Created on 2012-2-29

@author: zi.yez
'''
from django.db.models import Q
from dal.models import CMDB_AppInstance

class AppInstanceManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
    
    def getAppInstanceInfoByCondition(self,conditionDict):
        #host_name,cpu_core,memory,appServer_id
        condition = Q(flag = True)
        
        if conditionDict.has_key('host_name') and conditionDict['host_name'] is not None:
            condition.add(Q(host_name__contains = conditionDict['host_name']), Q.AND)
        if conditionDict.has_key('cpu_core') and conditionDict['cpu_core'] is not None:
            condition.add(Q(cpu_core = conditionDict['cpu_core']),Q.AND)
        if conditionDict.has_key('memory') and conditionDict['memory'] is not None:
            condition.add(Q(memory = conditionDict['memory']), Q.AND)
        if conditionDict.has_key('appserver_id') and conditionDict['appserver_id'] is not None:
            condition.add(Q(appserver_id = conditionDict['appserver_id']), Q.AND)
        
        return CMDB_AppInstance.objects.filter(condition)
    
    def insertAppInstanceInfo(self,appInstance):
        if appInstance.checkHostNameUnique(appInstance.host_name):
            #add logging
            pass
        #elif the foreignkey judgement ???
        else:
            appInstance.flag = True
            appInstance.save()
                
    def updateAppInstanceInfo(self,appInstanceInfo):
        try:
            existAppInstance = CMDB_AppInstance.objects.get(id = appInstanceInfo.id)
            existAppInstance = appInstanceInfo
            existAppInstance.gmtmodified = 'system'
        except:
            #add logging
            pass
    
    def deleteAppInstanceInfo(self,appInstanceId):
        try:
            appInstanceInfo = CMDB_AppInstance.objects.get(id = appInstanceId)
            appInstanceInfo.flag = False
            appInstanceInfo.gmtModified = 'system'
            appInstanceInfo.save() 
        except:
            #add logging
            pass
    
    def deleteAppInstanceInfoByAppServerId(self,appServerId):
        appInstanceTuple = CMDB_AppInstance.objects.filter(appserver_id = appServerId,flag = True)
        if appInstanceTuple:
            for appInstance in appInstanceTuple:
                appInstance.flag = False
                appInstance.gmtModified = 'system'
                appInstance.save()
        else:
            #add logging
            pass      