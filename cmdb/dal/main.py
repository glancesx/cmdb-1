'''
Created on 2012-2-25

@author: zi.yez
'''
import DictionaryManager
import models

if __name__ == '__main__':
    p = models.CMDB_Dictionary()
    
    p.key = 'AMD2'
    p.value = 'AMD XX11'
    p.key_type = 'CPU_TYPE'
    p.gmtCreator = 'zi.yez'
    dictionaryList = [p]
       
    DictionaryManager.DictionaryManager().insertDictionaryInfo(dictionaryList)
#    result = DictionaryManager.DictionaryManager().getDictionaryInfoAll()
#    print result[0].id
    #DictionaryManager.DictionaryManager().switchDictionaryInfoFlag(21, False)

    