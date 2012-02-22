# -*- coding:utf-8 -*-
from django.db import models

CPU_TYPE_CHOICES = (
                    (u'',u''),
                    );
IP_TYPE_CHOICES = (
                   (u'ip',u'public_ip_address'),
                   (u'vip',u'virtual_ip_address')
                   )
SERVER_TYPE_CHOICES = (
                       (u'ap',u'appserver'),
                       (u'ai',u'appinstance')
                       )

# Create your models here.
# 服务器硬件资源表
class AppServer(models.Model):
    host_name = models.CharField(max_length = 30);
    cpu_core = models.CharField(max_length = 10);
    cpu_type = models.CharField(max_length = 30,choices = CPU_TYPE_CHOICES);
    memory = models.CharField(max_length = 30);
    sn = models.CharField(max_length = 30);
    
# 服务器实例资源表   
class AppInstance(models.Model):
    host_name = models.CharField(max_length = 30);
    cpu_core = models.CharField(max_length = 30);
    memory = models.CharField(max_length = 30);
    appserver_id = models.ForeignKey(AppServer); 
    
# IP资源表
class Ip_Source(models.Model):
    ip = models.CharField(max_length = 39);
    ip_type = models.CharField(max_length = 20,choices = IP_TYPE_CHOICES);
    server = models.IntegerField();
    server_type = models.CharField(max_length = 20,choices= SERVER_TYPE_CHOICES);
    
# 硬盘硬件资源表
class Disc_Source(models.Model):
    number = models.IntegerField();
    size = models.BigIntegerField();
    raid = models.CharField(max_length = 10);
    raid_size = models.BigIntegerField();
    remark = models.CharField(max_length = 500);
    appserver_id = models.ForeignKey(AppServer);

# 服务器实例分区资源表
class Disc_Patition(models.Model):
    patition = models.CharField(max_length = 50);
    patition_size = models.BigIntegerField();
    patition_type = models.CharField(max_length = 20);
    appinstance_id = models.ForeignKey(AppInstance);

# 服务器字典表
class Dictionary(models.Model):
    key = models.CharField(max_length = 20);
    value = models.CharField(max_length = 50);
    key_type = models.CharField(max_length = 20);

# 服务器应用系统关联表    
class AppBiz(models.Model):
    env = models.ForeignKey(Dictionary);
    app = models.ForeignKey(Dictionary);
    app_source = models.URLField();
    appinstance_id = models.ForeignKey(AppInstance);
    
# DNS解析表
class Dns(models.Model):
    ip = models.CharField(max_length = 39);
    dns = models.URLField();
    env = models.ForeignKey(Dictionary);
    app = models.ForeignKey(Dictionary);