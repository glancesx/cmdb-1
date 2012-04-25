# -*- coding:utf-8 -*-
'''
Created on 2012-2-25

@author: zi.yez
'''
from biz.models import CMDB_Dictionary
from common.LogFactory import LogFactory
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist 

class DictionaryManager(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.logger = LogFactory(__name__)    
    
    #query the dictionary info by condition
    def getDictionaryInfoByCondition(self,conditionDict):
        condition = Q(flag = True)
        if conditionDict.has_key('id') and conditionDict['id'] is not None:
            condition.add(Q(id = conditionDict['id']),Q.AND)
        if conditionDict.has_key('key') and conditionDict['key'] is not None:
            condition.add(Q(key__iexact = conditionDict['key']), Q.AND)
        if conditionDict.has_key('key_type') and conditionDict['key_type'] is not None:            
            condition.add(Q(key_type = conditionDict['key_type']), Q.AND)
        if conditionDict.has_key('value') and conditionDict['value'] is not None:            
            condition.add(Q(value__icontains = conditionDict['value']), Q.AND)
            
        return CMDB_Dictionary.objects.filter(condition)
    
    #insert dictionary info and active it    
    def insertDictionaryInfo(self,dictionary):
        if not dictionary.checkKeyType(dictionary.key_type):
            self.logger.error(u'checkKeyType判断为True', u'checkKeyType判断为False', u'keyType非法，不是系统内已配置的值！')
        elif dictionary.checkKeyUnique(dictionary.key):
            self.logger.error(u'checkKeyUnique判断为False', u'checkKeyUnique判断为True', u'dictionary数据已存在,不能新增数据！')                    
        else:
            dictionary.flag = True
            dictionary.save()
    
    #update the dictionary info            
    def updateDictionaryInfo(self,dictionaryInfo):
        if not dictionaryInfo.checkKeyType(dictionaryInfo.key_type):
            self.logger.error(u'checkKeyType判断为True', u'checkKeyType判断为False', u'keyType非法，不是系统内已配置的值！')
            return
        
        try:
            existDict = CMDB_Dictionary.objects.get(id = dictionaryInfo.id,flag = True)
            existDict = dictionaryInfo
            existDict.save()            
        except ObjectDoesNotExist:
            self.logger.error(u'系统中存在id为 %d 的dictionary数据'%(dictionaryInfo.id), u'系统中不存在id为 %d 的dictionary数据'%(dictionaryInfo.id), '需要更新的数据不存在！') 
        except:
            self.logger.error(None, None, '其他异常！')           
    
    #delete the dictionary info        
    def deleteDictionaryInfo(self,keyId):        
        try:
            existDict = CMDB_Dictionary.objects.get(id = keyId,flag = True)
            existDict.flag = False
            existDict.gmtModifier = 'system'
            existDict.save()
        except ObjectDoesNotExist:
            self.logger.error(u'系统中存在id为 %d 的dictionary数据'%(keyId), u'系统中不存在id为 %d 的dictionary数据'%(keyId), '需要更新的数据不存在！') 
        except:
            self.logger.error(None, None, '其他异常！')        