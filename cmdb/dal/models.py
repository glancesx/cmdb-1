from django.db import models

# Create your models here.
# 服务器硬件资源表
class AppServerSource(models.Model):
    mainboard = models.CharField(maxlength = 30);
    cpu = models.CharField(maxlength = 30);
    disc = models.CharField(maxlength = 30);
    memory = models.CharField(maxlength = 30);
    ip = models.CharField(maxlength = 39);
    
# 服务器实例资源表   
class AppInstanceSource(models.Model):
    mainboard = models.CharField(maxlength = 30);
    cpu = models.CharField(maxlength = 30);
    disc = models.CharField(maxlength = 30);
    memory = models.CharField(maxlength = 30);
    ip = models.CharField(maxlength = 39);
    source_owner = models.ForeignKey(AppServerSource); 
    
#服务器字典表
class Dictionary(models.Model):
    name = models.CharField(maxlength = 20);
    value = models.CharField(maxlength = 20);

#服务器应用系统关联表    
class AppInstanceBiz(models.Model):
    env = models.CharField(maxlength = 30);
    app = models.CharField(maxlength = 30);
    app_source = models.URLField();
    
#DNS解析表
class Dns(models.Model):
    ip = models.CharField(maxlength = 16);
    dns = models.URLField;