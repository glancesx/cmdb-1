'''
Created on 2012-3-28

@author: yezi
'''
from biz.SourceManager import QuerySourceManager
from webservice.thriftservice import ttypes

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
            print appInfoList
            resultList = self.__putResult(appInfoList)
            cmdbInfoDoList += resultList
        return cmdbInfoDoList
    
    def updateCmdbAppInfo(self):
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
