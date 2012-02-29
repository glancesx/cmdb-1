# -*- coding:utf-8 -*-
'''
Created on 2012-2-25

@author: zi.yez
'''
from cmdb.dal.models import CMDB_Dictionary,KEY_TYPE_CHOICES
from django.db.models import Q

class DictionaryManager(object):
    '''
    classdocs
    '''
    def __init__(self):        
        pass
    
    def getDictionaryInfoByCondition(self,keyType,keyValue):
        condition = Q(flag = True)
        if keyType is not None:            
            condition.add(Q(key_type = keyType), Q.AND)
        if keyValue is not None:            
            condition.add(Q(value__icontains = keyValue), Q.AND)
        return CMDB_Dictionary.objects.filter(condition)    
    
    #insert dictionary info and active it    
    def insertDictionaryInfo(self,dictionaryList):
        dictionary = CMDB_Dictionary()
        for dictionary in dictionaryList:
            if self.__checkKeyType(dictionary.key_type):
                #add logging
                pass
            elif self.__checkUnique(dictionary.key):
                #add logging
                pass
            else:
                dictionary.flag = True 
                dictionary.save()
    
    #update the dictionary info            
    def updateDictionaryInfo(self,dictionaryInfo):
        if self.__checkKeyType(dictionaryInfo.key_type):
            #add logging
            return
        
        try:
            existDict = CMDB_Dictionary.objects.get(id = dictionaryInfo.id,flag = True)
            existDict = dictionaryInfo
            existDict.gmtModifier = 'system'
            existDict.save()            
        except:
            #add logging
            return
            
    
    #delete the dictionary info        
    def deleteDictionaryInfo(self,keyId):        
        try:
            existDict = CMDB_Dictionary.objects.get(id = keyId,flag = True)
            existDict.flag = False
            existDict.gmtModifier = 'system'
            existDict.save()
        except :
            #add logging
            return
    
    #check the key_type is in the tuple KEY_TYPE_CHOICES or not
    def __checkKeyType(self,keyType):
        checkFlag = True
        for keyTuple in KEY_TYPE_CHOICES:
            if keyType == keyTuple[0]:
                checkFlag = False
        return checkFlag
    
    #keep the key unique
    def __checkUnique(self,checkKey):
        return CMDB_Dictionary.objects.filter(key__iexact = checkKey,flag = True)           