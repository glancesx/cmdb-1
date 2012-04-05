'''
Created on 2012-3-18

@author: yezi
'''
from cmdb.dal.models import CMDB_AppServer,CMDB_AppInstance,CMDB_Ip_Source,CMDB_AppBiz
from cmdb.dal.AppServerManager import AppServerManager
from cmdb.dal.AppInstanceManager import AppInstanceManager
from cmdb.biz.RelationshipManager import RelationshipManager

def createAppServer():
    appServer = CMDB_AppServer()
    appServer.host_name = 'hztest001'
    appServer.cpu_core = 'Intel 4 Core'
    appServer.setCpuType('AMD')
    appServer.memory = '4G'
    appServer.sn = 'sn789397173499'
    AppServerManager().insertAppServerInfo(appServer)
    return appServer

def createAppInstance(appServer):
    appInstance = CMDB_AppInstance()
    appInstance.host_name = 'hztest001001'
    appInstance.cpu_core = 'Intel 2 Core'
    appInstance.memory = '1G'
    appInstance.setAppServerId(appServer.id)
    AppInstanceManager().insertAppInstanceInfo(appInstance)
    return appInstance

def createIpSource(appInstance):
    ipSource = CMDB_Ip_Source()
    ipSource.ip = '125.168.120.11'
    ipSource.setIpType('IP')
    ipSourceList = []
    ipSourceList.append(ipSource)
    RelationshipManager().mountAndInsertSource(appInstance, ipSourceList)
    
def createAppBiz(appInstance):
    appBiz = CMDB_AppBiz()
    appBiz.setApp('HADES')
    appBiz.setAppType('APACHE')
    appBiz.setEnv('PAT')
    appBiz.app_port = '80'
    appBiz.app_source = 'http://www.sina.com.cn'
    appBizList = []
    appBizList.append(appBiz)
    RelationshipManager().mountAndInsertSource(appInstance, appBizList)

if __name__ == '__main__':
    appServer = createAppServer()
    appInstance = createAppInstance(appServer)
    createIpSource(appInstance)
    createAppBiz(appInstance)
    
    pass