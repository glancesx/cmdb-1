# -*- coding:utf-8 -*-
'''
Created on 2012-3-4

@author: yezi
'''
from models import CMDB_Ip_Source
from models import CMDB_Dictionary
import DictionaryManager

if __name__ == '__main__':
    ipTypeInit = CMDB_Dictionary()
#    ipTypeInit.key = 'VIP'
#    ipTypeInit.key_type = 'IP_TYPE'
#    ipTypeInit.value = 'Virtual IP'
#    dictionaryList = []
#    dictionaryList.append(ipTypeInit)
#    DictionaryManager.DictionaryManager().insertDictionaryInfo(dictionaryList)
    
    ipSource = CMDB_Ip_Source()
    ipSource.ip = '125.10.2.13'
    
    ipSource.ip_type = CMDB_Dictionary.objects.get(key = 'VIP')
    
    ipSource.insertSource()