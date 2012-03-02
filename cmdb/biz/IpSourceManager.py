'''
Created on 2012-3-1

@author: zi.yez
'''
from cmdb.dal.models import CMDB_Ip_Source

class IpSourceManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
   
    def getIpSourceInfo(self,ipId):
        try:                
            return CMDB_Ip_Source.objects.get(id = ipId)
        except:
            #add logging
            return
   
    def insertIpSourceInfo(self,ipSourceList):
        ipSource = CMDB_Ip_Source()
        for ipSource in ipSourceList:
            if ipSource.checkIpUnique(ipSource.ip):
                #add logging
                pass
            else:
                ipSource.flag = True
                ipSource.save()
                
    def updateIpSourceInfo(self,ipSourceInfo):
        try:
            existIpInfo = CMDB_Ip_Source.objects.get(id = ipSourceInfo.id,flag = True)
            existIpInfo = ipSourceInfo
            existIpInfo.gmtmodified = 'system'
            existIpInfo.save()
        except:
            #add logging
            pass
    
    def deleteIpSourceInfo(self,ipId):
        try:
            ipSource = CMDB_Ip_Source.objects.get(id = ipId,flag = True)
            ipSource.flag = False
            ipSource.gmtmodified = 'system'
            ipSource.save()
        except:
            #add logging
            pass