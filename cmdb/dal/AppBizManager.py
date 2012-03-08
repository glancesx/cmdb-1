'''
Created on 2012-3-7

@author: zi.yez
'''
from django.db.models import Q

class AppBizManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def getAppBizByCondition(self,conditionDict):
        condition = Q()
        
        if conditionDict.has_key('') 
        return