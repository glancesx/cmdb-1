'''
Created on 2012-3-2

@author: zi.yez
'''
from dal.models import CMDB_Disc_Source
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
    
    def getDiscSourceInfo(self,conditionDict):
        condition = Q()
        if conditionDict.has_key('id') and conditionDict['id'] is not None:
            condition.add(Q(id = conditionDict['id']), Q.AND)
        if conditionDict.has_key('number') and conditionDict['number'] is not None:
            condition.add(Q(number = conditionDict['number']), Q.AND)
        if conditionDict.has_key('minsize') and conditionDict['minsize'] is not None:
            condition.add(Q(size__gte = conditionDict['minsize']), Q.AND)
        if conditionDict.has_key('maxsize') and conditionDict['maxsize'] is not None:
            condition.add(Q(size__lte = conditionDict['maxsize']), Q.AND)
        if conditionDict.has_key('raid') and conditionDict['raid'] is not None:
            condition.add(Q(raid = conditionDict['raid']), Q.AND)
        if conditionDict.has_key('min_raid_size') and conditionDict['min_raid_size'] is not None:
            condition.add(Q(raid_size__gte = conditionDict['min_raid_size']), Q.AND)
        if conditionDict.has_key('max_raid_size') and conditionDict['max_raid_size'] is not None:
            condition.add(Q(raid_size__lte = conditionDict['max_raid_size']), Q.AND)
        if conditionDict.has_key('remark') and conditionDict['remark'] is not None:
            condition.add(Q(remark__contains = conditionDict['remark']), Q.AND)
    
        return CMDB_Disc_Source.objects.filter(condition)
    
        