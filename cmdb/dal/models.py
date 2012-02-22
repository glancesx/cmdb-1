# -*- coding:utf-8 -*-
from django.db import models

KEY_TYPE_CHOICES = (
                    (u'CPU_TYPE',u'cpu_type class'),
                    (u'IP_TYPE',u'ip_type class'),
                    (u'SERVER_TYPE',u'server_type class'),
                    (u'RAID',u'raid type class'),
                    (u'PATITION_TYPE',u'patition_type class'),
                    (u'ENV',u'env class'),
                    (u'APP',u'app class'),
                    );

class Common(models.Model):
    gmtCreator = models.CharField(max_length = 32);
    gmtCreated = models.DateTimeField(auto_now_add = True);
    gmtModifier = models.CharField(max_length = 32);
    gmtModified = models.DateTimeField(auto_now = True);
    
    class Meta:
        abstract = True;
        
# Create your models here.
# 服务器字典表
class Dictionary(Common):
    key = models.CharField(max_length = 20,unique = True);
    value = models.CharField(max_length = 50);
    key_type = models.CharField(max_length = 20,choices = KEY_TYPE_CHOICES);

# 服务器硬件资源表
class AppServer(Common):
    host_name = models.CharField(max_length = 30, unique = True);
    cpu_core = models.CharField(max_length = 10);
    cpu_type = models.ForeignKey(Dictionary);
    memory = models.CharField(max_length = 30);
    sn = models.CharField(max_length = 30);
    
# 服务器实例资源表   
class AppInstance(Common):
    host_name = models.CharField(max_length = 30,unique = True);
    cpu_core = models.CharField(max_length = 30);
    memory = models.CharField(max_length = 30);
    appserver_id = models.ForeignKey(AppServer); 
    
# IP资源表
class Ip_Source(Common):
    ip = models.CharField(max_length = 39);
    ip_type = models.ForeignKey(Dictionary);
    server = models.IntegerField();
    server_type = models.CharField(max_length = 20);
    
# 硬盘硬件资源表
class Disc_Source(Common):
    number = models.IntegerField();
    size = models.BigIntegerField();
    raid = models.ForeignKey(Dictionary);
    raid_size = models.BigIntegerField();
    remark = models.CharField(max_length = 500);
    appserver_id = models.ForeignKey(AppServer);

# 服务器实例分区资源表
class Disc_Patition(Common):
    patition = models.CharField(max_length = 50);
    patition_size = models.BigIntegerField();
    patition_type = models.ForeignKey(Dictionary);
    appinstance_id = models.ForeignKey(AppInstance);

# 服务器应用系统关联表    
class AppBiz(Common):
    env = models.ForeignKey(Dictionary,related_name = 'env_set');
    app = models.ForeignKey(Dictionary,related_name = 'app_set');
    app_source = models.URLField();
    appinstance_id = models.ForeignKey(AppInstance);
    
# DNS解析表
class Dns(Common):
    ip = models.CharField(max_length = 39);
    dns = models.URLField();
    env = models.ForeignKey(Dictionary,related_name = 'env_set');
    app = models.ForeignKey(Dictionary,related_name = 'app_set');