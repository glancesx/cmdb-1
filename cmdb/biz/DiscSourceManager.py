'''
Created on 2012-3-2

@author: zi.yez
'''
from cmdb.dal.models import CMDB_Disc_Source

class DiscSourceManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def getDiscSourceInfo(self,discId):
        try:
            return CMDB_Disc_Source.objects.get(id = discId)
        except:
            #add logging
            pass
    
    def insertDiscSourceInfo(self,discSourceList):
        discSource = CMDB_Disc_Source()
        for discSource in discSourceList:
            if not discSource.checkRaidType(discSource.raid):
                #add logging
                pass
            else:
                discSource.flag = True
                discSource.save()
    
    def updateDiscSourceInfo(self,discSource):
        pass
    
    
        