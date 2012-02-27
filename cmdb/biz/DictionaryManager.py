# -*- coding:utf-8 -*-
'''
Created on 2012-2-25

@author: zi.yez
'''
from cmdb.dal.models import CMDB_Dictionary,KEY_TYPE_CHOICES

class DictionaryManager(object):
    '''
    classdocs
    '''
    def __init__(self):        
        pass
    
    #get all active dictionary info
    def getDictionaryInfoAll(self):
        return CMDB_Dictionary.objects.filter(flag = True)
    
    #get all inactive dictionary info
    def getDictionaryInfoAllFalse(self):        
        return CMDB_Dictionary.objects.filter(flag = False)
    
    #get dictionary info by keyType       
    def getDictionaryInfoByType(self,keyType):
        if keyType is None:
            #add logging
            return
        return CMDB_Dictionary.objects.filter(key_type = keyType,flag = True)
    
    #get dictionary info by value (like %s%)
    def getDictionaryInfoByValue(self,keyValue):
        if keyValue is None:
            #add logging
            return
        return CMDB_Dictionary.objects.filter(value__contains = keyValue,flag = True)
    
    #insert dictionary info and active it    
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
    
    #update the dictionary info            
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
    
    #active or inactive the dictionary info        
    def switchDictionaryInfoFlag(self,keyId,flagStatus):        
        existDict = CMDB_Dictionary.objects.get(id = keyId)
        if existDict:
            existDict.flag = flagStatus
            existDict.gmtModifier = 'system'
            existDict.save()
        else :
            #add logging
            return
    
    #check the key_type is in the tuple KEY_TYPE_CHOICES or not
    def checkKeyType(self,keyType):
        checkFlag = True
        for keyTuple in KEY_TYPE_CHOICES:
            if keyType == keyTuple[0]:
                checkFlag = False
        return checkFlag
    
    #keep the key unique
    def checkUnique(self,checkKey):
        checkFlag = False
        if CMDB_Dictionary.objects.filter(key = checkKey):
            checkFlag = True
        return checkFlag
    
            
            

            
        