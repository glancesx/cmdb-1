'''
Created on 2012-2-29

@author: zi.yez
'''
from django.db.models import Q
from cmdb.dal.models import CMDB_AppInstance

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
        if conditionDict.has_key('appServer_id') and conditionDict['appServer_id'] is not None:
            condition.add(Q(appServer_id = conditionDict['appServer_id']), Q.AND)
        
        return CMDB_AppInstance.objects.filter(condition)
    
    def insertAppInstanceInfo(self):
        
        return
        