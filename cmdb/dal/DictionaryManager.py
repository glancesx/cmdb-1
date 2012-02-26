'''
Created on 2012-2-25

@author: zi.yez
'''
from models import CMDB_Dictionary,KEY_TYPE_CHOICES

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
        return dictionary.objects.filter(flag = True)
    
    def getDictionaryInfoAllFalse(self):
        dictionary = CMDB_Dictionary()
        return dictionary.objects.filter(flag = False)
           
    def getDictionaryInfoByType(self,keyType):
        if keyType is None:
            #add logging
            return        
        dictionary = CMDB_Dictionary()
        return dictionary.objects.filter(key_type = keyType,flag = True)
    
    def getDictionaryInfoByValue(self,keyValue):
        if keyValue is None:
            #add logging
            return
        dictionary = CMDB_Dictionary()
        return dictionary.objects.filter(value__contains = keyValue,flag = True)
        
    def insertDictionaryInfo(self,dictionaryList):
        dictionary = CMDB_Dictionary()
        for dictionary in dictionaryList:
            if self.checkKeyType(dictionary.key_type):
                #add logging
                return    
            dictionary.save()
                
    def updateDictionaryInfo(self,dictionaryInfo):
        if self.checkKeyType(dictionaryInfo.key_type):
            #add logging
            return
        
        dictionary = CMDB_Dictionary()
        existDict = dictionary.objects.get(id = dictionaryInfo.id)
        if existDict :
            updateDict = existDict(dictionaryInfo)
            updateDict.save()
        else:
            #add logging
            return
            
    def switchDictionaryInfoFlag(self,keyId,flagStatus):
        dictionary = CMDB_Dictionary()
        existDict = dictionary.objects.get(id = keyId)
        if existDict:
            updateDict = existDict(flag = flagStatus)
            updateDict.save()
        else :
            #add logging
            return
    
    def checkKeyType(self,keyType):
        checkFlag = True
        for keyTuple in KEY_TYPE_CHOICES:
            if keyType == keyTuple(0):
                checkFlag = False
        return checkFlag
    
            
            

            
        