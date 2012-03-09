'''
Created on 2012-3-7

@author: zi.yez
'''
from django.db.models import Q
from cmdb.dal.models import CMDB_AppBiz

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
        condition = Q(flag = True)
        appBiz = CMDB_AppBiz()
        
        if conditionDict.has_key('env'):
            envValue = appBiz.getEnv(conditionDict['env'])
            condition.add(Q(env = envValue.id), Q.AND)
        if conditionDict.has_key('app'):
            appValue = appBiz.getApp(conditionDict['app'])
            condition.add(Q(app = appValue.id), Q.AND)
        if conditionDict.has_key('app_type'):
            appTypeValue = appBiz.getAppType(conditionDict['app_type'])
            condition.add(Q(app_type = appTypeValue.id), Q.AND)
        if conditionDict.has_key('app_port'):
            condition.add(Q(app_port = conditionDict['app_port']), Q.AND)
        if conditionDict.has_key('app_source'):
            condition.add(Q(app_source__contains = conditionDict['app_source']), Q.AND)
        
        return CMDB_AppBiz.objects.filter(condition)