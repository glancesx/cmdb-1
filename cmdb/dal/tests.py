# -*- coding:utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from cmdb.dal.DictionaryManager import *

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
        
#        
#    def test_update_fail(self):
#        """
#        测试修改数据失败，表中不存在对应key的数据
#        """
#        self.assertEqual(1 + 1, 2)
#        
#    def test_update_fail_flagFalse(self):
#        """
#        测试修改数据失败，表中存在对应key的数据且flag为False的数据
#        """
#        self.assertEqual(1 + 1, 2)
#    
#    def test_query_byCondition(self):
#        """
#        测试根据查询条件组合查询
#        """
#        self.assertEqual(1 + 1, 2)
#    
#    def test_delete_success(self):
#        """
#        测试‘删除’数据成功，表中存在对应key且flag为True的数据
#        """
#        self.assertEqual(1 + 1, 2)
#        
#    def test_delete_fail(self):
#        """
#        测试‘删除’数据失败，表中不存在对应key的数据
#        """
#        self.assertEqual(1 + 1, 2)
#    
#    def test_delete_fail_flagFalse(self):
#        """
#        测试‘删除’数据失败，表中存在对应key且flag为false的数据
#        """
#        self.assertEqual(1 + 1, 2)
        
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
