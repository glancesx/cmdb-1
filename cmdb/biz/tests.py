
# -*- coding:utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from dal.models import CMDB_Dictionary,CMDB_AppServer
from dal.DictionaryManager import DictionaryManager
from django.core.exceptions import ObjectDoesNotExist
from dal.AppServerManager import AppServerManager

class DalDictionaryTest(TestCase):
    def test_insert_success_new(self):
        """
        测试插入数据成功，表中不存在相同key的数据
        """
        dictionary = self.__prepareData()
        DictionaryManager().insertDictionaryInfo(dictionary)
        query = CMDB_Dictionary.objects.get(key = dictionary.key,flag = True)
        self.assertEqual(dictionary.value, query.value)        
        self.__deleteData(dictionary)        
            
    def test_insert_fail_unique(self):
        """
        测试插入数据失败，表中存在相同key且flag为True的数据
        """
        dictionary = self.__prepareData()
        dictionary.save()
        dictionary2 = self.__prepareData()
        DictionaryManager().insertDictionaryInfo(dictionary2)
        query = CMDB_Dictionary.objects.filter(key = dictionary2.key,flag = True)
        self.assertEqual(len(query), 1)
        self.__deleteData(dictionary)
        
    def test_insert_sucess_flagFalse(self):
        """
        测试插入数据成功，表中存在相同key且flag为False的数据
        """
        dictionary = self.__prepareData()        
        dictionary.save()
        dictionary.flag = False
        dictionary.save()
        
        dictionary2 = self.__prepareData()
        DictionaryManager().insertDictionaryInfo(dictionary2)
        query = CMDB_Dictionary.objects.filter(key = dictionary.key)
        self.assertEqual(len(query), 2)
        self.__deleteData(dictionary)
        
    def test_update_success(self):
        """
        测试修改数据成功，表中存在对应key且flag为True的数据
        """
        dictionary = self.__prepareData()        
        dictionary.save()
        
        dictionary.key = 'INTEL 2'
        DictionaryManager().updateDictionaryInfo(dictionary)     
        query = CMDB_Dictionary.objects.get(key = dictionary.key,flag = True)
        self.assertEqual(query.key, dictionary.key)
        self.__deleteData(dictionary)
        
    def test_update_fail(self):
        """
        测试修改数据失败，表中不存在对应key的数据
        """
        dictionary = self.__prepareData() 
        dictionary.key = 'INTEL 2'
        DictionaryManager().updateDictionaryInfo(dictionary)
        #self.assertRaises( ObjectDoesNotExist, DictionaryManager().updateDictionaryInfo, dictionary)
        query = CMDB_Dictionary.objects.filter(key = dictionary.key,flag = True)
        self.assertEqual(len(query), 0)
                
        
    def test_update_fail_flagFalse(self):
        """
        测试修改数据失败，表中存在对应key的数据且flag为False的数据
        """
        dictionary = self.__prepareData()
        dictionary.flag = False
        dictionary.save()
        
        dictionary.key = 'INTEL 2'
        DictionaryManager().updateDictionaryInfo(dictionary)
        self.assertRaises( ObjectDoesNotExist, CMDB_Dictionary.objects.get, key = dictionary.key)
        self.__deleteData(dictionary)
    
    def test_query_byCondition(self):
        """
        测试根据查询条件组合查询
        """
        dictionary = self.__prepareData()
        dictionary.save()
        
        conditionDict = {}
        conditionDict['id'] = CMDB_Dictionary.objects.all()[0].id
        result = DictionaryManager().getDictionaryInfoByCondition(conditionDict)
        self.assertEqual(conditionDict['id'],result[0].id)
    
        conditionDict['key'] = 'amd 2'
        result = DictionaryManager().getDictionaryInfoByCondition(conditionDict)
        self.assertEqual('AMD 2',result[0].key)
        
        conditionDict.clear()
        conditionDict['key_type'] = 'CPU_TYPE'
        result = DictionaryManager().getDictionaryInfoByCondition(conditionDict)
        self.assertEqual(result[0].key_type, conditionDict['key_type'])
        
        conditionDict['value'] = 'amd 2'
        result = DictionaryManager().getDictionaryInfoByCondition(conditionDict)
        self.assertEqual(result[0].value,'AMD 2 CPU')
        
        self.__deleteData(dictionary)
        
    def test_delete_success(self):
        """
        测试‘删除’数据成功，表中存在对应key且flag为True的数据
        """
        dictionary = self.__prepareData()
        dictionary.save()
        
        DictionaryManager().deleteDictionaryInfo(dictionary.id)
        result = CMDB_Dictionary.objects.get(id = dictionary.id)
        self.assertEqual(result.flag, False)
        self.__deleteData(dictionary)
        
    def test_delete_fail(self):
        """
        测试‘删除’数据失败，表中不存在对应key的数据
        """
        dictionary = self.__prepareData()
        DictionaryManager().deleteDictionaryInfo(dictionary.id)
        self.assertRaises( ObjectDoesNotExist, CMDB_Dictionary.objects.get, key = dictionary.key)
    
    def test_delete_fail_flagFalse(self):
        """
        测试‘删除’数据失败，表中存在对应key且flag为false的数据
        """
        dictionary = self.__prepareData()
        dictionary.flag = False
        dictionary.save()
        
        firstModifyTime = CMDB_Dictionary.objects.get(id = dictionary.id).gmtModified
        DictionaryManager().deleteDictionaryInfo(dictionary.id)
        result = CMDB_Dictionary.objects.get(id = dictionary.id)
        self.assertEqual(firstModifyTime,result.gmtModified)
        
    def __prepareData(self):
        #prepare the test data
        dictionary = CMDB_Dictionary()
        dictionary.key = 'AMD 2'
        dictionary.key_type = 'CPU_TYPE'
        dictionary.value = 'AMD 2 CPU'
        dictionary.flag = True
        dictionary.gmtCreated = 'DalDictionaryTest'  
        
        return dictionary
    
    def __deleteData(self,dictionary):
        if len(CMDB_Dictionary.objects.filter(key = dictionary.key)):
            dictionary.delete() 


class DalCMDBAppServerTest(TestCase):  
    def test_insert_success(self):
        """
        测试插入数据成功，表中不存在相同key的数据
        """
        appServer = self.__prepareData()
        AppServerManager().insertAppServerInfo(appServer)
        result = CMDB_AppServer.objects.get(id = appServer.id)
        self.assertEqual(result.id , appServer.id)
        self.__deleteData(appServer)
    
    def test_insert_fail_unique(self):
        """
        测试插入数据失败，表中存在相同host_name且flag为True的数据
        """
        appServer = self.__prepareData()
        appServer.save()
        appServer2 = self.__prepareData()
        AppServerManager().insertAppServerInfo(appServer2)
        result = CMDB_AppServer.objects.filter(host_name = appServer.host_name)

        self.assertEqual(len(result),1)
        self.__deleteData(appServer)
    
    def test_insert_sucess_flagFalse(self):
        """
        测试插入数据成功，表中存在相同host_name且flag为False的数据
        """
        appServer = self.__prepareData()
        appServer.flag = False
        appServer.save()
        appServer2 = self.__prepareData()
        AppServerManager().insertAppServerInfo(appServer2)
        result = CMDB_AppServer.objects.filter(host_name = appServer.host_name)

        self.assertEqual(len(result),2)
        self.__deleteData(appServer)
        self.__deleteData(appServer2)
    
    def test_update_success(self):
        """
        测试修改数据成功，表中存在对应host_name且flag为True的数据
        """
        pass
    
#     def test_update_fail(self):
#         """
#         测试修改数据失败，表中不存在对应key的数据
#         """
#         pass
    
#     def test_update_fail_flagFalse(self):
#         """
#         测试修改数据失败，表中存在对应key的数据且flag为False的数据
#         """
#         pass
    
#     def test_query_byCondition(self):
#         """
#         测试根据查询条件组合查询
#         """
#         pass
    
#     def test_delete_success(self):
#         """
#         测试‘删除’数据成功，表中存在对应key且flag为True的数据
#         """
#         pass
        
#     def test_delete_fail(self):
#         """
#         测试‘删除’数据失败，表中不存在对应key的数据
#         """
#         pass
    
#     def test_delete_fail_flagFalse(self):
#         """
#         测试‘删除’数据失败，表中存在对应key且flag为false的数据
#         """
#         pass
    
    def __prepareData(self):
        if not CMDB_Dictionary.objects.all():
            self.__initDictionary()

        appServer = CMDB_AppServer()
        appServer.host_name = 'hztest001'
        appServer.cpu_core = 'Intel 4 Core'
        appServer.setCpuType('AMD')
        appServer.memory = '4G'
        appServer.sn = 'sn789397173499'
        appServer.flag = True

        return appServer
        
    def __deleteData(self,appServer):
        if CMDB_AppServer.objects.filter(host_name = appServer.host_name):
            appServer.delete()
    
    def __initDictionary(self):
        DictionaryList = (
                    ['CPU_TYPE',['AMD','INTEL']],
                    ['IP_TYPE',['VIP','IP']],
                    ['RAID',['SSD','SATA']],
                    ['PATITION_TYPE',['SYSTEM','USER']],
                    ['ENV',['PRD','PAT','TESTA','TESTB','TESTC','DEV']],
                    ['APP',['HADES','AEGIS','DUBBO','NAPOLI']],
                    ['APP_TYPE',['APACHE','TOMCAT','DATABASE']],
                    )

        for keyType in DictionaryList:
            for key in keyType[1]:
                dictionary = CMDB_Dictionary()
                dictionary.key_type = keyType[0]
                dictionary.key = key                
                DictionaryManager().insertDictionaryInfo(dictionary)