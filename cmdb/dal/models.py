# -*- coding:utf-8 -*-
from django.db import models
import datetime

KEY_TYPE_CHOICES = (
                    (u'CPU_TYPE',u'cpu_type class'),
                    (u'IP_TYPE',u'ip_type class'),
                    (u'SERVER_TYPE',u'server_type class'),
                    (u'RAID',u'raid type class'),
                    (u'PATITION_TYPE',u'patition_type class'),
                    (u'ENV',u'env class'),
                    (u'APP',u'app class'),
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
        
    class Meta:
        app_label = 'dal'
        abstract = True
        
# Create your models here.
# 服务器字典表
class CMDB_Dictionary(Common):
    key = models.CharField(max_length = 20)
    value = models.CharField(max_length = 50)
    key_type = models.CharField(max_length = 20,choices = KEY_TYPE_CHOICES)
    
    class Meta:
        app_label = 'dal'
        ordering = ["id","key_type"]

# 服务器硬件资源表
class CMDB_AppServer(Common):
    host_name = models.CharField(max_length = 30)
    cpu_core = models.CharField(max_length = 10)
    cpu_type = models.ForeignKey(CMDB_Dictionary)
    memory = models.CharField(max_length = 30)
    sn = models.CharField(max_length = 30)
    
# 服务器实例资源表   
class CMDB_AppInstance(Common):
    host_name = models.CharField(max_length = 30)
    cpu_core = models.CharField(max_length = 30)
    memory = models.CharField(max_length = 30)
    appserver_id = models.ForeignKey(CMDB_AppServer) 
    
# IP资源表
class CMDB_Ip_Source(Common):
    ip = models.CharField(max_length = 39)
    ip_type = models.ForeignKey(CMDB_Dictionary)
    server = models.IntegerField()
    server_type = models.CharField(max_length = 20)
    
# 硬盘硬件资源表
class CMDB_Disc_Source(Common):
    number = models.IntegerField()
    size = models.BigIntegerField()
    raid = models.ForeignKey(CMDB_Dictionary)
    raid_size = models.BigIntegerField()
    remark = models.CharField(max_length = 500)
    appserver_id = models.ForeignKey(CMDB_AppServer)

# 服务器实例分区资源表
class CMDB_Disc_Patition(Common):
    patition = models.CharField(max_length = 50)
    patition_size = models.BigIntegerField()
    patition_type = models.ForeignKey(CMDB_Dictionary)
    appinstance_id = models.ForeignKey(CMDB_AppInstance)

# 服务器应用系统关联表    
class CMDB_AppBiz(Common):
    env = models.ForeignKey(CMDB_Dictionary,related_name = 'env_set')
    app = models.ForeignKey(CMDB_Dictionary,related_name = 'app_set')
    app_source = models.URLField()
    appinstance_id = models.ForeignKey(CMDB_AppInstance)
    
# DNS解析表
class CMDB_Dns(Common):
    ip = models.CharField(max_length = 39)
    dns = models.URLField()
    env = models.ForeignKey(CMDB_Dictionary,related_name = 'env_dns_set')
    app = models.ForeignKey(CMDB_Dictionary,related_name = 'app_dns_set')