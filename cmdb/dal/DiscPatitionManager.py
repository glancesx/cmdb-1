'''
Created on 2012-3-2

@author: zi.yez
'''
from cmdb.dal.models import CMDB_Disc_Patition
from django.db.models import Q

class DiscSourceManager(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def getDiscPatitionInfo(self,conditionDict):
        condition = Q()
        if conditionDict.has_key('id') and conditionDict['id'] is not None:
            condition.add(Q(id = conditionDict['id']), Q.AND)
        if conditionDict.has_key('patition') and conditionDict['patition'] is not None:
            condition.add(Q(patition = conditionDict['patition']), Q.AND)
        if conditionDict.has_key('min_patition_size') and conditionDict['min_patition_size'] is not None:
            condition.add(Q(patition_size__gte = conditionDict['min_patition_size']), Q.AND)
        if conditionDict.has_key('max_patition_size') and conditionDict['max_patition_size'] is not None:
            condition.add(Q(patition_size__lte = conditionDict['max_patition_size']), Q.AND)
        if conditionDict.has_key('patition_type') and conditionDict['patition_type'] is not None:
            condition.add(Q(patition_type = conditionDict['patition_type']), Q.AND)       
    
        return CMDB_Disc_Patition.objects.filter(condition)
    
    
        