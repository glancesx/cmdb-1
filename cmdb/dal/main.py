'''
Created on 2012-2-25

@author: zi.yez
'''
import DictionaryManager
import models

if __name__ == '__main__':
    p = models.CMDB_Dictionary()
    
    p.key = 'AMD1'
    p.value = 'AMD XX'
    p.key_type = 'CPU_TYPE'
    p.gmtCreator = 'zi.yez'
    dictionaryList = [p]
       
    DictionaryManager.DictionaryManager().insertDictionaryInfo(dictionaryList)
    