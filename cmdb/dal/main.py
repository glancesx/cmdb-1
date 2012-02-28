'''
Created on 2012-2-25

@author: zi.yez
'''
from cmdb.biz.DictionaryManager import DictionaryManager
import models

if __name__ == '__main__':
    p = models.CMDB_Dictionary()
    
#    p.key = 'AMD3'
#    p.value = 'AMD XX11'
#    p.key_type = 'CPU_TYPE'
#    p.gmtCreator = 'zi.yez'
#    dictionaryList = [p]
          
#   result = DictionaryManager.DictionaryManager().getDictionaryInfoAll()
#   print result[0].id
    #DictionaryManager.DictionaryManager().switchDictionaryInfoFlag(21, False)
    keyType = 'CPU_TYPE'
    keyValue = None
    result = DictionaryManager().getDictionaryInfoByCondition(keyType, keyValue)
    
    print result[0].value
    