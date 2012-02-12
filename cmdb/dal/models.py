from django.db import models

# Create your models here.
# 服务器硬件资源表
class AppServer(models.Model):
    host_name = models.CharField(maxlength = 30);
    cpu_core = models.CharField(maxlength = 10);
    cpu_type = models.CharField(maxlength = 30);
    memory = models.CharField(maxlength = 30);
    sn = models.CharField(maxlength = 30);
    
# 服务器实例资源表   
class AppInstance(models.Model):
    host_name = models.CharField(maxlength = 30);
    cpu_core = models.CharField(maxlength = 30);
    memory = models.CharField(maxlength = 30);
    appserver_id = models.ForeignKey(AppServer); 
    
# IP资源表
class Ip_Source(models.Model):
    ip = models.CharField(maxlength = 39);
    ip_type = models.CharField(maxlength = 20);
    server = models.IntegerField();
    server_type = models.CharField(20);
    
# 硬盘硬件资源表
class Disc_Source(models.Model):
    number = models.IntegerField();
    size = models.BigIntegerField();
    raid = models.CharField(maxlength = 10);
    raid_size = models.BigIntegerField;
    remark = models.CharField(maxlength = 500);
    appserver_id = models.ForeignKey(AppServer);

# 服务器实例分区资源表
class Disc_Patition(models.Model):
    patition = models.CharField(maxlength = 50);
    patition_size = models.BigIntegerField();
    patition_type = models.CharField(maxlength = 20);
    appinstance_id = models.ForeignKey(AppInstance);

# 服务器字典表
class Dictionary(models.Model):
    key = models.CharField(maxlength = 20);
    value = models.CharField(maxlength = 50);
    key_type = models.CharField(maxlength = 20);

# 服务器应用系统关联表    
class AppBiz(models.Model):
    env = models.ForeignKey(Dictionary);
    app = models.ForeignKey(Dictionary);
    app_source = models.URLField();
    appinstance_id = models.ForeignKey(AppInstance);
    
# DNS解析表
class Dns(models.Model):
    ip = models.CharField(maxlength = 39);
    dns = models.URLField;
    env = models.ForeignKey(Dictionary);
    app = models.ForeignKey(Dictionary);