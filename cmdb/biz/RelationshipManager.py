'''
Created on 2012-3-3

@author: yezi
'''
from dal.models import CMDB_Relationship,CMDB_AppBiz,CMDB_AppInstance
from django.db.models import Q

class RelationshipManager(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass

    def getRelationship(self,conditionDict):
        condition = Q(flag = True)
        if conditionDict.has_key('force') and conditionDict['force'] is not None:
            condition.add(Q(force = conditionDict['force']), Q.AND)
        if conditionDict.has_key('force_table') and conditionDict['force_table'] is not None:
            condition.add(Q(force_table = conditionDict['force_table']), Q.AND)
        if conditionDict.has_key('source') and conditionDict['source'] is not None:
            condition.add(Q(source = conditionDict['source']), Q.AND) 
        if conditionDict.has_key('source_table') and conditionDict['source_table'] is not None:
            condition.add(Q(source_table = conditionDict['source_table']), Q.AND)    
        
        return CMDB_Relationship.objects.filter(condition)
    
    def disRelationship(self,forceObject,sourceObject):
        relationship = CMDB_Relationship()
        relationship.force = forceObject.id
        relationship.force_table = forceObject.tableName()
        relationship.source = sourceObject.id
        relationship.source_table = sourceObject.tableName()
        
        try:
            existRelationship = CMDB_Relationship.objects.get(force = relationship.force,force_table = relationship.force_table,source = relationship.source,source_table = relationship.source_table)
            existRelationship.flag = False
            existRelationship.save()
        except:
            #add logging
            pass    
    
    def insertRelationship(self,forceObject,sourceObject):
        relationship = CMDB_Relationship()
        relationship.force = forceObject.id
        relationship.force_table = forceObject.tableName()
        relationship.source = sourceObject.id
        relationship.source_table = sourceObject.tableName()
        
        if relationship.checkRsUnique(relationship.force, relationship.force_table, relationship.source, relationship.source_table):
            #add logging
            pass
        else:
            relationship.flag = True
            relationship.save()
    
    
    def mountAndInsertSource(self,forceObject,sourceObject):
        if forceObject and sourceObject:
            getattr(sourceObject,'insertSource')()
            self.mountSource(forceObject,sourceObject)
        else:
            #add logging
            pass
    
    def mountSource(self, forceObject, sourceObject):
        if type(sourceObject) == CMDB_AppBiz and type(forceObject) == CMDB_AppInstance:
            if sourceObject.checkUnique(forceObject):
                self.insertRelationship(forceObject, sourceObject)
            else:
                #add log
                return
        else:
            self.insertRelationship(forceObject, sourceObject)
        
    def disMountSource(self,forceObject,sourceObject):
        self.disRelationship(forceObject, sourceObject)
        try:
            getattr(sourceObject,'deleteSource')()
        except:
            #add logging
            pass
            