# -*- coding:utf-8 -*-
from django.db import models
import datetime
import logging

logger = logging.getLogger(__name__)

KEY_TYPE_CHOICES = (
                    (u'CPU_TYPE',u'cpu_type class'),
                    (u'IP_TYPE',u'ip_type class'),                   
                    (u'RAID',u'raid type class'),
                    (u'PATITION_TYPE',u'patition_type class'),
                    (u'ENV',u'env class'),
                    (u'APP',u'app class'),
                    (u'APP_TYPE',u'app type class'),
                    )

class Common(models.Model):
    gmtCreator = models.CharField(max_length = 32)    
    gmtCreated = models.DateTimeField()
    gmtModifier = models.CharField(max_length = 32)    
    gmtModified = models.DateTimeField()
    flag = models.BooleanField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps as '%Y-%m-%d %H:%M:%S' '''
        if not self.id :
            self.gmtCreated = datetime.datetime.strftime(datetime.datetime.today(),'%Y-%m-%d %H:%M:%S')
        self.gmtModified = datetime.datetime.strftime(datetime.datetime.today(),'%Y-%m-%d %H:%M:%S')
        super(Common,self).save(*args, **kwargs)
    
    def tableName(self):
        return (self.Meta.app_label + '_' + self.__class__.__name__).upper()
    
    class Meta:
        app_label = 'dal'
        abstract = True
      
# Create your models here.
# 服务器字典表
class CMDB_Dictionary(Common):
    key = models.CharField(max_length = 20)
    value = models.CharField(max_length = 50)
    key_type = models.CharField(max_length = 20,choices = KEY_TYPE_CHOICES)
    
    #check the key_type is in the tuple KEY_TYPE_CHOICES or not
    def checkKeyType(self,keyType):
        booleanFlag = False
        for keyTuple in KEY_TYPE_CHOICES:
            if keyTuple[0] == keyType:
                booleanFlag = True
        return booleanFlag
    
    #check the key is unique or not
    def checkKeyUnique(self,checkKey):
        return CMDB_Dictionary.objects.filter(key__iexact = checkKey,flag = True)
    
    class Meta:
        app_label = 'dal'
        ordering = ['id','key_type']

# 服务器硬件资源表
class CMDB_AppServer(Common):
    host_name = models.CharField(max_length = 30)
    cpu_core = models.CharField(max_length = 30)
    cpu_type = models.ForeignKey(CMDB_Dictionary)
    memory = models.CharField(max_length = 30)
    sn = models.CharField(max_length = 30)
        
    def checkHostNameUnique(self,hostName):                
        return CMDB_AppServer.objects.filter(host_name__iexact = hostName,flag = True)
    
    def getCpuType(self,cpuType):
        try:
            return CMDB_Dictionary.objects.get(key__iexact = cpuType,key_type = 'CPU_TYPE',flag = True)
        except:
            #add logging
            return
        
    def setCpuType(self,cpuType):
        self.cpu_type = self.getCpuType(cpuType)
    
    class Meta:
        app_label = 'dal'
        ordering = ['id']
        
# 服务器实例资源表   
class CMDB_AppInstance(Common):
    host_name = models.CharField(max_length = 30)
    cpu_core = models.CharField(max_length = 30)
    memory = models.CharField(max_length = 30)
    appserver_id = models.ForeignKey(CMDB_AppServer)
    
    def checkHostNameUnique(self,hostName):
        return CMDB_AppInstance.objects.filter(host_name__iexact = hostName,flag = True)
    
    def getAppServerId (self,appServerId):
        try:
            return CMDB_AppServer.objects.get(id = appServerId,flag = True)
        except:
            #add logging
            return
    
    def setAppServerId(self,appServerId):
        self.appserver_id = self.getAppServerId(appServerId)
    
    class Meta:
        app_label = 'dal'
        ordering = ['id']

# IP资源表
class CMDB_Ip_Source(Common):
    ip = models.IPAddressField()
    ip_type = models.ForeignKey(CMDB_Dictionary)
    
    def insertSource(self):
        if self.checkIpUnique(self.ip):
            #add logging
            pass
        else:
            self.flag = True
            self.save()
            
    def deleteSource(self):
        try:
            ipSource = CMDB_Ip_Source.objects.get(self.id,flag = True)
            ipSource.flag = False
            ipSource.save()
        except:
            #add logging
            pass
    
    def updateSource(self):
        try:
            ipSource = CMDB_Ip_Source.objects.get(self.id,flag = True)
            ipSource = self
            ipSource.save()
        except:
            #add logging
            pass                
    
    def checkIpUnique(self,checkIp):
        return len(CMDB_Ip_Source.objects.filter(ip = checkIp,flag = True))
    
    def getIpType(self,ipType):
        try:
            return CMDB_Dictionary.objects.get(key__iexact = ipType,key_type='IP_TYPE',flag = True)
        except:
            #add logging
            return
    def setIpType(self,ipType):
        self.ip_type = self.getIpType(ipType)
    
    class Meta:
        app_label = 'dal'
        
# 硬盘硬件资源表
class CMDB_Disc_Source(Common):
    number = models.IntegerField()
    size = models.BigIntegerField()
    raid = models.ForeignKey(CMDB_Dictionary)
    raid_size = models.BigIntegerField()
    remark = models.CharField(max_length = 500)
    
    def insertSource(self):
        self.flag = True
        self.save()
    
    def deleteSource(self):
        try:
            discSource = CMDB_Disc_Source.objects.get(self.id,flag = True)
            discSource.flag = False
            discSource.save()
        except:
            #add logging
            pass
    
    def updateSource(self):
        try:
            discSource = CMDB_Disc_Source.objects.get(self.id,flag = True)
            discSource = self
            discSource.save()
        except:
            #add logging
            pass
    
    def getRaid(self,raidValue):
        try:
            return CMDB_Dictionary.objects.get(key__iexact = raidValue,key_type='RAID',flag = True)
        except:
            #add logging
            return
        
    def setRaid(self,raidValue):
        self.raid = self.getRaid(raidValue)
    
    class Meta:
        app_label = 'dal'          

# 服务器实例分区资源表
class CMDB_Disc_Patition(Common):
    patition = models.CharField(max_length = 50)
    patition_size = models.BigIntegerField()
    patition_type = models.ForeignKey(CMDB_Dictionary)    
    
    def insertSource(self):
        self.flag = True
        self.save()
    
    def deleteSource(self):
        try:
            discSource = CMDB_Disc_Patition.objects.get(self.id,flag = True)
            discSource.flag = False
            discSource.save()
        except:
            #add logging
            pass
    
    def updateSource(self):
        try:
            discSource = CMDB_Disc_Patition.objects.get(self.id,flag = True)
            discSource = self
            discSource.save()
        except:
            #add logging
            pass
    
    def getPatitionType(self,patitionType):
        try:
            return CMDB_Dictionary.objects.get(key__iexact = patitionType,key_type='PATITION_TYPE',flag = True)
        except:
            #add logging
            return
    
    def setPatitionType(self,patitionType):
        self.patition_type = self.getPatitionType(patitionType)
    
    class Meta:
        app_label = 'dal'     
    
# 服务器应用系统关联表    
class CMDB_AppBiz(Common):
    env = models.ForeignKey(CMDB_Dictionary,related_name = 'env_set')
    app = models.ForeignKey(CMDB_Dictionary,related_name = 'app_set')
    app_type = models.ForeignKey(CMDB_Dictionary,related_name = 'app_type_set')
    app_port = models.IntegerField()
    app_source = models.CharField(max_length = 256)

    def insertSource(self):
        self.flag = True
        self.save()
    
    def deleteSource(self):
        try:
            discSource = CMDB_Disc_Patition.objects.get(self.id,flag = True)
            discSource.flag = False
            discSource.save()
        except:
            #add logging
            pass
    
    def updateSource(self):
        try:
            discSource = CMDB_Disc_Patition.objects.get(self.id,flag = True)
            discSource = self
            discSource.save()
        except:
            #add logging
            pass
    
    def setEnv(self,envValue):
        self.env = self.getEnv(envValue)
    
    def getEnv(self,envValue):
        try:
            return CMDB_Dictionary.objects.get(key__iexact = envValue,key_type = 'ENV',flag = True)
        except:
            #add logging
            return
        
    def setApp(self,appValue):
        self.app = self.getApp(appValue)
        
    def getApp(self,appValue):
        try:
            return CMDB_Dictionary.objects.get(key__iexact = appValue,key_type = 'APP',flag = True)
        except:
            #add logging
            return
        
    def setAppType(self,appTypeValue):
        self.app_type = self.getAppType(appTypeValue)
        
    def getAppType(self,appTypeValue):
        try:
            return CMDB_Dictionary.objects.get(key__iexact = appTypeValue,key_type = 'APP_TYPE',flag = True)
        except:
            #add logging
            return
    
    def checkUnique(self,appInstance):
        #find all the appBiz under the appInstance
        existAppBizList = CMDB_Relationship.objects.filter(force = appInstance.id,force_table = appInstance.tableName(),source_table = self.tableName(),flag = True)
        #check whether the appBiz is unique by app_port
        if existAppBizList:
            for existAppBiz in existAppBizList:
                if existAppBiz.app_port == self.app_port:
                    #add log
                    return False
        return True
    
    class Meta:
        app_label = 'dal'
    
# DNS解析表
class CMDB_Dns(Common):
    ip = models.IPAddressField()
    dns = models.URLField()
    env = models.ForeignKey(CMDB_Dictionary,related_name = 'env_dns_set')
    app = models.ForeignKey(CMDB_Dictionary,related_name = 'app_dns_set')

# 资源挂载关系表    
class CMDB_Relationship(Common):
    force = models.IntegerField()
    force_table = models.CharField(max_length = 32)
    source = models.IntegerField()
    source_table = models.CharField(max_length = 32)
    
    def checkRsUnique(self,checkForce,checkForceTable,checkSource,checkSourceTable):
        return CMDB_Relationship.objects.filter(force = checkForce,force_table = checkForceTable, source = checkSource,source_table = checkSourceTable,flag = True)
    
    class Meta:
        app_label = 'dal'

#select 'drop '||object_type||' '||object_name||';' drop_sql from user_objects where object_type in ('TABLE','TRIGGER','SEQUENCE');     