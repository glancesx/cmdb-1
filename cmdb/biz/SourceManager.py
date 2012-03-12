'''
Created on 2012-3-6

@author: zi.yez
'''

from cmdb.dal.IpSourceManager import *
from cmdb.biz.RelationshipManager import *
from cmdb.dal.AppInstanceManager import *
from cmdb.dal.AppBizManager import *

class QuerySourceManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def queryAppInstanceByIp(self,ip):        
        relationship = self.__getRelationshipByIp(ip)
        if relationship is None:
            #add logging
            return
               
        conditionDict = {}
        conditionDict['id'] = relationship.force        
        appInstanceList = AppInstanceManager().getAppInstanceInfoByCondition(conditionDict)
        if appInstanceList is None:
            #add logging
            return
        
        return appInstanceList[0]
        
    def queryAppBizByIp(self,ip):
        appBiz = CMDB_AppBiz()        
        relationship = self.__getRelationshipByIp(ip)
        if relationship is None:
            #add logging
            return
               
        conditionDict = {}
        conditionDict['force'] = relationship.force
        conditionDict['force_table'] = relationship.force_table
        conditionDict['source_table'] = appBiz.tableName()
                
        bizRelationshipList = RelationshipManager().getRelationship(conditionDict)
        if bizRelationshipList is None:
            #add logging
            return
        conditionDict.clear()
        conditionDict['id'] =  bizRelationshipList[0].source       
        appBizList = AppBizManager().getAppBizByCondition(conditionDict)
        
        if appBizList is None:
            #add logging
            return
        return appBizList[0]
        
    #Get the relationship by ip address        
    def __getRelationshipByIp(self,ip):
        conditionDict = {'ip':ip}
        ipSourceList = IpSourceManager().getIpSourceInfo(conditionDict)        
        if ipSourceList is None:
            #add logging
            return
               
        ipSource = ipSourceList[0]
        appInstance = CMDB_AppInstance()        
        conditionDict['source'] = ipSource.id
        conditionDict['source_table'] = ipSource.tableName()
        conditionDict['force_table'] = appInstance.tableName()        
        relationshipList = RelationshipManager().getRelationship(conditionDict)        
        if relationshipList is None:
            return
        
        return relationshipList[0]
    
    def queryAppInstanceByEnv(self,envValue,appValue,appTypeValue):        
        relationship = self.__getRelationshipByEnv(envValue,appValue,appTypeValue)
        if relationship is None:
            #add logging
            return
               
        conditionDict = {}
        conditionDict['id'] = relationship.force        
        appInstanceList = AppInstanceManager().getAppInstanceInfoByCondition(conditionDict)
        if appInstanceList is None:
            #add logging
            return
        
        return appInstanceList[0]
    
    def queryIpSourceByEnv(self,envValue,appValue,appTypeValue):
        relationship = self.__getRelationshipByEnv(envValue,appValue,appTypeValue)
        if relationship is None:
            #add logging
            return
        
        conditionDict = {}
        ipSource = CMDB_Ip_Source()
        conditionDict['force'] = relationship.force
        conditionDict['force_table'] = relationship.force_table
        conditionDict['source_table'] = ipSource.tableName()
        
        ipRelationship = RelationshipManager().getRelationship(conditionDict)
        if ipRelationship is None:
            #add logging
            return
        
        conditionDict.clear()
        conditionDict['id'] = ipRelationship[0].source
        ipSourceList = IpSourceManager().getIpSourceInfo(conditionDict)
        if ipSourceList is None:
            #add logging
            return        
        
        return ipSourceList[0]
    
    #Get the relationship by Env
    def __getRelationshipByEnv(self,envValue,appValue,appTypeValue):
        conditionDict = {'env':envValue,'app':appValue,'app_type':appTypeValue}
        appBizList = AppBizManager.getAppBizByCondition(conditionDict)
        if appBizList is None:
            #add logging
            return
        
        appBiz = appBizList[0]
        appInstance = CMDB_AppInstance()
        conditionDict['source'] = appBiz.id
        conditionDict['source_table'] = appBiz.tableName()
        conditionDict['force_table'] = appInstance.tableName()        
        relationshipList = RelationshipManager().getRelationship(conditionDict)        
        if relationshipList is None:
            #add logging
            return
        
        return relationshipList[0]


class UpdateSourceManager(object):
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
        
    def updateSource(self,env,app,appType,port,appSource,appInstanceId):
        #create AppBiz instance
        appBiz = CMDB_AppBiz()
        appBiz.setEnv(env)
        appBiz.setApp(app)
        appBiz.setAppType(appType)
        appBiz.app_port = port
        appBiz.app_source = appSource
        #get relationship between CMDB_AppInstance and CMDB_AppBiz
        conditionDict = {}
        conditionDict['force'] = appInstanceId
        appInstance = CMDB_AppInstance()
        conditionDict['force_table'] = appInstance.tableName()
        conditionDict['source_table'] = appBiz.tableName()
        bizRelationshipList = RelationshipManager().getRelationship(conditionDict)
        if bizRelationshipList is None:
            #add logging
            pass
        else:
            #update CMDB_AppBiz
            appBiz.id = bizRelationshipList[0].source
            appBiz.updateSource()
    
    def delSource(self,env,app,appType,port,appSource,appInstanceId):
        #create CMDB_AppBiz instance
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
            #get relationship between CMDB_AppInstance and CMDB_AppBiz
            appInstance = appInstanceList[0]
            RelationshipManager().disMountSource(appInstance, appBiz)
        