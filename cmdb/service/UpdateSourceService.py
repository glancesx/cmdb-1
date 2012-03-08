'''
Created on 2012-3-8

@author: zi.yez
'''
from cmdb.dal.models import CMDB_AppBiz
from cmdb.dal.AppInstanceManager import *
from cmdb.biz.RelationshipManager import *

class UpdateSourceService(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def createSourceAndMount(self,env,app,appType,port,appSource,appInstanceId):
        #create AppBiz instance
        appBiz = CMDB_AppBiz()
        appBiz.setEnv(env)
        appBiz.setApp(app)
        appBiz.setAppType(appType)
        appBiz.app_port = port
        appBiz.app_source = appSource                
        #get CMDB_AppInstance
        conditionDict = {'id':appInstanceId}
        appInstanceList = AppInstanceManager.getAppInstanceInfoByCondition(conditionDict)
        if appInstanceList is None:
            #add logging
            pass
        else:
            appInstance = appInstanceList[0]
            sourceObjectList = []
            sourceObjectList.append(appBiz)
            #insert into DAL_CMDB_APPBIZ
            #insert into DAL_CMDB_RELATIONSHIP
            RelationshipManager().mountAndInsertSource(appInstance, sourceObjectList)
        
        