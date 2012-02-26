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
        pass
    
    def getDictionaryInfoAll(self):
        return CMDB_Dictionary.objects.filter(flag = True)
    
    def getDictionaryInfoAllFalse(self):        
        return CMDB_Dictionary.objects.filter(flag = False)
           
    def getDictionaryInfoByType(self,keyType):
        if keyType is None:
            #add logging
            return
        return CMDB_Dictionary.objects.filter(key_type = keyType,flag = True)
    
    def getDictionaryInfoByValue(self,keyValue):
        if keyValue is None:
            #add logging
            return
        return CMDB_Dictionary.objects.filter(value__contains = keyValue,flag = True)
        
    def insertDictionaryInfo(self,dictionaryList):
        dictionary = CMDB_Dictionary()
        for dictionary in dictionaryList:
            if self.checkKeyType(dictionary.key_type):
                #add logging
                return
            if self.checkUnique(dictionary.key):
                #add logging
                return            
            dictionary.flag = True 
            dictionary.save()
                
    def updateDictionaryInfo(self,dictionaryInfo):
        if self.checkKeyType(dictionaryInfo.key_type):
            #add logging
            return
                
        existDict = CMDB_Dictionary.objects.get(id = dictionaryInfo.id)
        if existDict :
            existDict = dictionaryInfo
            existDict.gmtModifier = 'system'
            existDict.save()
        else:
            #add logging
            return
            
    def switchDictionaryInfoFlag(self,keyId,flagStatus):        
        existDict = CMDB_Dictionary.objects.get(id = keyId)
        if existDict:
            existDict.flag = flagStatus
            existDict.gmtModifier = 'system'
            existDict.save()
        else :
            #add logging
            return
    
    def checkKeyType(self,keyType):
        checkFlag = True
        for keyTuple in KEY_TYPE_CHOICES:
            if keyType == keyTuple[0]:
                checkFlag = False
        return checkFlag
    
    def checkUnique(self,checkKey):
        checkFlag = True
        if CMDB_Dictionary.objects.get(key = checkKey):
            checkFlag = False
        return checkFlag
    
            
            

            
        