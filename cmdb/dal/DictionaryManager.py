'''
Created on 2012-2-25

@author: zi.yez
'''
from models import CMDB_Dictionary

class DictionaryManager(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def getDictionaryInfoAll(self):               
        dictionary = CMDB_Dictionary()
        return dictionary.objects.all()
    
    def getDictionaryInfoByType(self,keyType):
        if keyType is None:
            #add logging
            return        
        dictionary = CMDB_Dictionary()
        return dictionary.objects.filter(key_type = keyType)
    
    def getDictionaryInfoByValue(self,keyValue):
        if keyValue is None:
            #add logging
            return
        dictionary = CMDB_Dictionary()
        return dictionary.objects.filter(value__contains = keyValue)
        
    def insertDictionaryInfo(self,dictionaryList):
        dictionary = CMDB_Dictionary()
        for dictionary in dictionaryList:
            dictionary.save()
            
    
            
            

            
        