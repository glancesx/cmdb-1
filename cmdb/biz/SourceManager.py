'''
Created on 2012-3-6

@author: zi.yez
'''

from dal.models import CMDB_Ip_Source,CMDB_AppInstance,CMDB_AppBiz
from dal.IpSourceManager import IpSourceManager
from dal.AppInstanceManager import AppInstanceManager
from dal.AppBizManager import AppBizManager
from biz.RelationshipManager import RelationshipManager

class AppInfo(object):
    def __init__(self,appInstance = None,appBizList = [],ipSource = None):
        self.appInstance = appInstance
        self.appBizList = appBizList
        self.ipSource = ipSource
    

class QuerySourceManager(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    def getAppInfoList(self,ip = None,app = None,app_type = None,env = None):
        if ip:
            return self.getAppInfoListByIp(ip)
        elif app and app_type and env:
            return self.getAppInfoListByEnv(app,app_type,env)
        else:
            return
     
    def getAppInfoListByIp(self,ip):
        appInstance = self.getAppInstanceByIp(ip)
        appBizList = self.getAppBizListByAppInstance(appInstance)
        ipSource = self.getIpSourceByAppInstance(appInstance)
        appInfoList = []
        appInfoList.append(AppInfo(appInstance,appBizList,ipSource))
        
        return appInfoList
     
    def getAppInfoListByEnv(self,env,app,app_type):
        appInstanceList = self.getAppInstanceListByEnv(env,app,app_type)
        appInfoList = []
        for appInstance in appInstanceList:
            appInfo = AppInfo(appInstance,self.getAppBizListByAppInstance(appInstance),self.getIpSourceByAppInstance(appInstance))
            appInfoList.append(appInfo)
        return appInfoList

    def getAppInstanceByIp(self,ip):        
        relationship = self.__getRelationshipByIp(ip)
        if not relationship:
            #add logging
            return
               
        conditionDict = {}
        conditionDict['id'] = relationship.force        
        appInstanceList = AppInstanceManager().getAppInstanceInfoByCondition(conditionDict)
        if not appInstanceList:
            #add logging
            return
        
        return appInstanceList[0]

    def getAppInstanceListByEnv(self,envValue,appValue,appTypeValue):        
        relationshipList = self.__getRelationshipByEnv(envValue,appValue,appTypeValue)
        if not relationshipList:
            #add logging
            return
        appInstanceList = []
        for relationship in relationshipList:
            conditionDict = {}
            conditionDict['id'] = relationship.force        
            resultList = AppInstanceManager().getAppInstanceInfoByCondition(conditionDict)
            if not resultList:
                #add logging
                return
            appInstanceList += resultList
            
        return appInstanceList
    
    def getAppBizListByAppInstance(self,appInstance):
        appBiz = CMDB_AppBiz()
        conditionDict = {}
        conditionDict['force'] = appInstance.id
        conditionDict['force_table'] = appInstance.tableName()
        conditionDict['source_table'] = appBiz.tableName()
        
        bizRelationshipList = RelationshipManager().getRelationship(conditionDict)
        if not bizRelationshipList:
            #add logging
            return
        conditionDict.clear()
        conditionDict['id'] =  bizRelationshipList[0].source       
        appBizList = AppBizManager().getAppBizByCondition(conditionDict)
        
        return appBizList
    
    def getIpSourceByAppInstance(self,appInstance):
        ipSource = CMDB_Ip_Source()
        conditionDict = {}
        conditionDict['force'] = appInstance.id
        conditionDict['force_table'] = appInstance.tableName()
        conditionDict['source_table'] = ipSource.tableName()
        
        ipRelationshipList = RelationshipManager().getRelationship(conditionDict)
        if not ipRelationshipList:
            #add logging
            return
        conditionDict.clear()
        conditionDict['id'] =  ipRelationshipList[0].source
        ipSourceList = IpSourceManager().getIpSourceInfo(conditionDict)
        if not ipSourceList:
            #add logging
            return
        
        return ipSourceList[0]
        
    #Get the relationship by ip address        
    def __getRelationshipByIp(self,ip):
        conditionDict = {'ip':ip}
        ipSourceList = IpSourceManager().getIpSourceInfo(conditionDict)        
        if not ipSourceList:
            #add logging
            return
               
        ipSource = ipSourceList[0]
        appInstance = CMDB_AppInstance()        
        conditionDict['source'] = ipSource.id
        conditionDict['source_table'] = ipSource.tableName()
        conditionDict['force_table'] = appInstance.tableName()        
        relationshipList = RelationshipManager().getRelationship(conditionDict)        
        if not relationshipList:
            return
        
        return relationshipList[0]

    #Get the relationship by Env
    def __getRelationshipListByEnv(self,envValue,appValue,appTypeValue):
        conditionDict = {'env':envValue,'app':appValue,'app_type':appTypeValue}
        appBizList = AppBizManager.getAppBizByCondition(conditionDict)
        if not appBizList:
            #add logging
            return
        
        appInstance = CMDB_AppInstance()
        relationshipList = []
        for appBiz in appBizList:
            conditionDict['source'] = appBiz.id
            conditionDict['source_table'] = appBiz.tableName()
            conditionDict['force_table'] = appInstance.tableName()        
            relationshipList2 = RelationshipManager().getRelationship(conditionDict)        
            if not relationshipList2:
                #add logging
                pass
            else:
                relationshipList += relationshipList2
        
        return relationshipList


class UpdateSourceManager(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    def modifyAppBizSource(self,appBizList,appInstance):
        conditionDict = {}
        conditionDict['force'] = appInstance.id
        appInstance = CMDB_AppInstance()
        appBiz = CMDB_AppBiz()
        conditionDict['force_table'] = appInstance.tableName()
        conditionDict['source_table'] = appBiz.tableName()
        bizRelationshipList = RelationshipManager().getRelationship(conditionDict)
        if not bizRelationshipList:
            for appBiz in appBizList:
                self.createAndMountAppBizSource(appBiz, appInstance)
        else:
            existAppBizIdList = []
            for bizRelationship in bizRelationshipList:
                existAppBizIdList.append(bizRelationship.source)
                
            for appBiz in appBizList:
                if appBiz.id in existAppBizIdList:
                    self.updateAppBizSource(appBiz, appInstance)
                else:
                    self.createAndMountAppBizSource(appBiz, appInstance)
    
    def createAndMountAppBizSource(self,appBiz,appInstance):          
        RelationshipManager().mountAndInsertSource(appInstance, appBiz)
        
    def updateAppBizSource(self,appBiz,appInstance):
        #get relationship between CMDB_AppInstance and CMDB_AppBiz
        conditionDict = {}
        conditionDict['force'] = appInstance.id
        conditionDict['force_table'] = appInstance.tableName()
        conditionDict['source_id'] = appBiz.id
        conditionDict['source_table'] = appBiz.tableName()
        bizRelationshipList = RelationshipManager().getRelationship(conditionDict)
        if not bizRelationshipList:
            #add logging
            pass
        else:
            #update CMDB_AppBiz
            appBiz.updateSource()
    
    def delAppBizSource(self,appBiz,appInstance):
        #get relationship between CMDB_AppInstance and CMDB_AppBiz
        conditionDict = {}
        conditionDict['force'] = appInstance.id
        conditionDict['force_table'] = appInstance.tableName()
        conditionDict['source_id'] = appBiz.id
        conditionDict['source_table'] = appBiz.tableName()
        bizRelationshipList = RelationshipManager().getRelationship(conditionDict)
        if not bizRelationshipList:
            #add logging
            pass
        else:
            RelationshipManager().disMountSource(appInstance, appBiz)