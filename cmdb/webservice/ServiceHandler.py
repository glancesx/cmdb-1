'''
Created on 2012-3-28

@author: yezi
'''
from biz.SourceManager import QuerySourceManager,UpdateSourceManager
from webservice.thriftservice import ttypes
from biz.models import CMDB_AppBiz,CMDB_Ip_Source
from biz.AppInstanceManager import AppInstanceManager

class AppManagerServiceHandler(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def getCmdbAppInfo(self,cmdbQueryBoList):
        cmdbInfoDoList = []
        for cmdbQueryBo in cmdbQueryBoList:
            appInfoList = QuerySourceManager().getAppInfoList(cmdbQueryBo.ip, cmdbQueryBo.app, cmdbQueryBo.app_type, cmdbQueryBo.env)
            resultList = self.__putResult(appInfoList)
            cmdbInfoDoList += resultList
        return cmdbInfoDoList
    
    def updateCmdbAppInfo(self,cmdbInfoDOList):
        for cmdbInfoDO in cmdbInfoDOList:
            appInstance = self.__putAppInstance(cmdbInfoDO)
            appBizList = self.__putAppBizList(cmdbInfoDO.cmdbAppBizList)
            if appInstance and appBizList:
                UpdateSourceManager().modifyAppBizSource(appBizList, appInstance)
            else:
                #add log
                pass
    
    def __putResult(self,appInfoList):
        CmdbInfoDOList = []
        for appInfo in appInfoList:
            CmdbInfoDOList.append(ttypes.CmdbInfoDO(appInfo.appInstance.id,appInfo.appInstance.host_name,appInfo.appInstance.cpu_core,appInfo.appInstance.memory,self.__putCmdbIp(appInfo.ipSource),self.__putCmdbAppBizList(appInfo.appBizList)))
        return CmdbInfoDOList
    
    def __putCmdbIp(self,ipSource):
        return ttypes.CmdbIp(ipSource.id,ipSource.ip,ipSource.ip_type.key)
    
    def __putCmdbAppBizList(self,appBizList):
        cmdbAppBizList = []
        for appBiz in appBizList:
            cmdbAppBizList.append(ttypes.CmdbAppBiz(appBiz.id,appBiz.env.key,appBiz.app.key,appBiz.app_type.key,appBiz.app_port,appBiz.app_source))
        return cmdbAppBizList
    
    def __putAppBizList(self,cmdbAppBizList):
        appBizList = []
        for cmdbAppBiz in cmdbAppBizList:
            appBiz = CMDB_AppBiz()
            appBiz.id = cmdbAppBiz.id
            appBiz.setEnv(cmdbAppBiz.env)
            appBiz.setAppType(cmdbAppBiz.app_type)
            appBiz.app_port = cmdbAppBiz.app_port
            appBiz.app_source = cmdbAppBiz.app_source
            appBiz.setApp(cmdbAppBiz.app)
            appBizList.append(appBiz)
        
        return appBizList
    
    def __putIpSource(self,cmdbIp):
        ipSource = CMDB_Ip_Source()
        ipSource.id = cmdbIp.id
        ipSource.ip = cmdbIp.ip
        ipSource.setIpType(cmdbIp.ip_type)
        
        return ipSource
    
    def __putAppInstance(self,cmdbInfoDO):
        conditionDict = {}
        conditionDict['id'] = cmdbInfoDO.appInstanceId
        conditionDict['host_name'] = cmdbInfoDO.host_name
        appInstanceList = AppInstanceManager().getAppInstanceInfoByCondition(conditionDict)
        if appInstanceList:
            return appInstanceList[0]
        else:
            raise