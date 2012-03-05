'''
Created on 2012-3-3

@author: yezi
'''
from cmdb.dal.models import CMDB_Relationship

class RelationshipManager(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def mountSource(self,forceObject,sourceObject):
        relationship = CMDB_Relationship()
        relationship.force = forceObject.id
        relationship.force_table = forceObject.__class__.__name__
        relationship.source = sourceObject.id
        relationship.source_table = sourceObject.__class__.__name__
        
        if relationship.checkRsUnique(relationship.force, relationship.force_table, relationship.source, relationship.source_table):
            #add logging
            pass
        else:
            relationship.flag = True
            relationship.save()
    
    def mountAndInsertSource(self,forceObject,sourceObjectList):
        for sourceObject in sourceObjectList:
            self.mountSource(forceObject,sourceObject)
            getattr(sourceObject,'insertObject')(sourceObject)
        
            
    def __disRelationship(self,forceObject,sourceObject):
        relationship = CMDB_Relationship()
        relationship.force = forceObject.id
        relationship.force_table = forceObject.__class__.__name__
        relationship.source = sourceObject.id
        relationship.source_table = sourceObject.__class__.__name__
        
        try:
            existRelationship = CMDB_Relationship.objects.get(force = relationship.force,force_table = relationship.force_table,source = relationship.source,source_table = relationship.source_table)
            existRelationship.flag = False
            existRelationship.save()
        except:
            #add logging
            pass
        
    def disMountSource(self,forceObject,sourceObject):
        self.__disRelationship(forceObject, sourceObject)
        try:
            getattr(sourceObject,'deleteSource')(sourceObject.id)
        except:
            #add logging
            pass
        
            