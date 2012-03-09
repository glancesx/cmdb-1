'''
Created on 2012-3-6

@author: zi.yez
'''
from cmdb.dal.models import CMDB_AppBiz
from cmdb.dal.IpSourceManager import *
from cmdb.biz.RelationshipManager import *
from cmdb.dal.AppInstanceManager import *
from cmdb.dal.AppBizManager import *

class QuerySourceService(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def queryAppInstanceByIp(self,ip):
        appInstance = CMDB_AppInstance()
        relationship = self.__getRelationshipByIp(ip,appInstance.tableName())
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
        appInstance = CMDB_AppInstance()
        relationship = self.__getRelationshipByIp(ip,appInstance.tableName())
        if relationship is None:
            #add logging
            return
               
        conditionDict = {}
        conditionDict['force'] = relationship.force
        conditionDict['force_table'] = appInstance.tableName()
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
    
    def queryAppInstanceByEnv(self,envValue,appValue,appTypeValue):
        
        return
    
    
    #Get the relationship by ip address        
    def __getRelationshipByIp(self,ip,forceTable):
        conditionDict = {'ip':ip}
        ipSourceList = IpSourceManager().getIpSourceInfo(conditionDict)        
        if ipSourceList is None:
            #add logging
            return
               
        ipSource = ipSourceList[0]        
        conditionDict['source'] = ipSource.id
        conditionDict['source_table'] = ipSource.tableName()
        conditionDict['force_table'] = forceTable        
        relationshipList = RelationshipManager().getRelationship(conditionDict)        
        if relationshipList is None:
            return
        
        return relationshipList[0]
    
    
    
    def __getRelationshipByEnv(self,envValue,appValue,appTypeValue,forceTable):
        conditionDict = {'env':envValue,'app':appValue,'app_type':appTypeValue}
        appBizList = AppBizManager.getAppBizByCondition(conditionDict)
        if appBizList is None:
            #add logging
            return
        
        appBiz = appBizList[0]
        conditionDict['source'] = appBiz.id
        conditionDict['source_table'] = appBiz.tableName()
        conditionDict['force_table'] = forceTable        
        relationshipList = RelationshipManager().getRelationship(conditionDict)        
        if relationshipList is None:
            return
        
        return relationshipList[0]
        