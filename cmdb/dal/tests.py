# -*- coding:utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from cmdb.dal.models import CMDB_Dictionary

class DalDictionaryTest(TestCase):
    #prepare the test data
    dictionary = CMDB_Dictionary()
    
    def test_insert_success_new(self):
        """
        测试插入数据成功，表中不存在相同key的数据
        """
        
        self.assertEqual(1 + 1, 2)
    
    def test_insert_fail_unique(self):
        """
        测试插入数据失败，表中存在相同key且flag为True的数据
        """
        self.assertEqual(1 + 1, 2)
        
    def test_insert_sucess_flagFalse(self):
        """
        测试插入数据成功，表中存在相同key且flag为False的数据
        """
        self.assertEqual(1 + 1, 2)
        
    def test_update_success(self):
        """
        测试修改数据成功，表中存在相同key且flag为True的数据
        """
        self.assertEqual(1 + 1, 2)
        
    def test_update_fail(self):
        """
        测试修改数据失败，表中不存在相同key的数据
        """
        self.assertEqual(1 + 1, 2)
        
    def test_update_fail_flagFalse(self):
        """
        测试修改数据失败，表中存在相同key的数据且flag为False的数据
        """
        self.assertEqual(1 + 1, 2)
    
    def test_query_byCondition(self):
        """
        """
        self.assertEqual(1 + 1, 2)
        