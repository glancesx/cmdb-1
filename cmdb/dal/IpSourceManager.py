'''
Created on 2012-3-1

@author: zi.yez
'''
from dal.models import CMDB_Ip_Source
from django.db.models import Q

class IpSourceManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
   
    def getIpSourceInfo(self,conditionDict):        
        condition = Q(flag = True)
        
        if conditionDict.has_key('id') and conditionDict['id'] is not None:
            condition.add(Q(id = conditionDict['id']), Q.AND)
        if conditionDict.has_key('ip') and conditionDict['ip'] is not None:
            condition.add(Q(ip = conditionDict['ip']), Q.AND)
        if conditionDict.has_key('ip_type') and conditionDict['ip_type'] is not None:
            condition.add(Q(ip_type = condition['ip_type']),Q.AND)        
        
        return  CMDB_Ip_Source.objects.filter(condition)
