from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Accountinfo(models.Model):
    #user = models.OneToOneField(User)
    uid = models.CharField('用户统一ID',max_length=30,unique= True)
    device = models.CharField('设备标识',max_length=100,blank=True)
    apns_token = models.CharField('苹果推送Token',max_length=100,blank=True)
    reject_tone = models.CharField('拒接电话语言',max_length=300,blank=True)
    