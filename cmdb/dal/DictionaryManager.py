# -*- coding:utf-8 -*-
'''
Created on 2012-2-25

@author: zi.yez
'''
from cmdb.dal.models import CMDB_Dictionary
from django.db.models import Q

class DictionaryManager(object):
    '''
    classdocs
    '''
    def __init__(self):        
        pass
    
    def getDictionaryInfoByCondition(self,conditionDict):
        condition = Q(flag = True)
        if conditionDict.has_key('key_type') and conditionDict['key_type'] is not None:            
            condition.add(Q(key_type = conditionDict['key_type']), Q.AND)
        if conditionDict.has_key('value') and conditionDict['value'] is not None:            
            condition.add(Q(value__icontains = conditionDict['value']), Q.AND)
        return CMDB_Dictionary.objects.filter(condition)    
    
    #insert dictionary info and active it    
    def insertDictionaryInfo(self,dictionary):
        if not dictionary.checkKeyType(dictionary.key_type):
            #add logging
            pass
        elif dictionary.checkKeyUnique(dictionary.key):
            #add logging
            pass
        else:
            dictionary.flag = True 
            dictionary.save()
    
    #update the dictionary info            
    def updateDictionaryInfo(self,dictionaryInfo):
        if not dictionaryInfo.checkKeyType(dictionaryInfo.key_type):
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