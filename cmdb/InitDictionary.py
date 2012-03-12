'''
Created on 2012-3-12

@author: zi.yez
'''

from cmdb.dal.DictionaryManager import CMDB_Dictionary,DictionaryManager

def initDictionary(DictionaryList):
    for keyType in DictionaryList:
        for key in keyType[1]:
            dictionary = CMDB_Dictionary()
            dictionary.key_type = keyType[0]
            dictionary.value = key                
            DictionaryManager().insertDictionaryInfo(dictionary)


if __name__ == '__main__':
    DictionaryList = (
                      ['CPU_TYPE',['AMD','INTEL']],
                      ['IP_TYPE',['VIP','IP']],
                      ['RAID',['SSD','SATA']],
                      ['PATITION_TYPE',['SYSTEM','USER']],
                      ['ENV',['PRD','PAT','TESTA','TESTB','TESTC','DEV']],
                      ['APP',['HADES','AEGIS','DUBBO','NAPOLI']],
                      ['APP_TYPE',['APACHE','TOMCAT','DATABASE']],
                      )
    
    initDictionary(DictionaryList)
    
    