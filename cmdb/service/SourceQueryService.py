'''
Created on 2012-3-6

@author: zi.yez
'''
from cmdb.dal.models import CMDB_AppBiz
from cmdb.dal.IpSourceManager import *
from cmdb.biz.RelationshipManager import *
from cmdb.dal.AppInstanceManager import *
from cmdb.dal.AppBizManager import *

class SourceQueryService(object):
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
        relationship = self.__getRelationshipByIp(ip,appInstance)
        if relationship is None:
            #add logging
            return
               
        conditionDict = {}
        conditionDict['id'] = relationship.force        
        appInstanceTuple = AppInstanceManager().getAppInstanceInfoByCondition(conditionDict)
        if appInstanceTuple is None:
            #add logging
            return
        
        return appInstanceTuple[0]
        
    def queryAppBizByIp(self,ip):
        appBiz = CMDB_AppBiz()
        appInstance = CMDB_AppInstance()
        relationship = self.__getRelationshipByIp(ip,appInstance)
        if relationship is None:
            #add logging
            return
               
        conditionDict = {}
        conditionDict['force'] = relationship.force
        conditionDict['force_table'] = appInstance.__class__.__name__
        conditionDict['source_table'] = appBiz.__class__.__name__
                
        bizRelationshipTuple = RelationshipManager().getRelationship(conditionDict)
        if bizRelationshipTuple is None:
            #add logging
            return
        conditionDict.clear()
        conditionDict['id'] =  bizRelationshipTuple[0].source       
        appBizTuple = AppBizManager().getAppBizByCondition(conditionDict)
        
        if appBizTuple is None:
            #add logging
            return
        return appBizTuple[0]
        
    def __getRelationshipByIp(self,ip,forceObject):
        conditionDict = {'ip':ip}
        ipSourceTuple = IpSourceManager().getIpSourceInfo(conditionDict)
        
        if ipSourceTuple is None:
            #add logging
            return
        
        ipSource = ipSourceTuple[0]
        conditionDict['source'] = ipSource.id
        conditionDict['source_table'] = ipSource.__class__.__name__
        conditionDict['force_table'] = forceObject.__class__.__name__        
        relationshipTuple = RelationshipManager().getRelationship(conditionDict)
        
        if relationshipTuple is None:
            return
        return relationshipTuple[0]
        
    
    
        
         
        
        
        