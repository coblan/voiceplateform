from django.db import models
from django.contrib.auth.models import User
from helpers.director.model_func.cus_fields.jsonable import JsonAbleField

# Create your models here.
class Accountinfo(models.Model):
    #user = models.OneToOneField(User)
    uid = models.CharField('用户统一ID',max_length=30,unique= True)
    device = models.CharField('设备标识',max_length=100,blank=True)
    apns_token = models.CharField('苹果推送Token',max_length=100,blank=True)
    reject_tone = models.TextField('拒接电话语音',blank=True)

MSG_STATUS=(
    (0,'初始化'),
    (1,'已获取'),
    (2,'已完成'),
)

class VoiceMsgList(models.Model):
    uid = models.CharField('相关用户UID',max_length=30)
    #uid = models.IntegerField('相关用户UID',)
    channel = models.CharField('频道名',max_length=30,)
    status = models.IntegerField('状态',default=0,choices=MSG_STATUS)
    createtime = models.DateTimeField('创建时间',auto_now_add=True)
    extra_msg = models.TextField('额外信息',blank=True)
    

#class ChannelList(models.Model):
    #name = models.CharField('频道名',max_length=30,)
    #starter = models.IntegerField('发起人UID',)
    #createtime = models.DateTimeField('创建时间',auto_now_add=True)

CALLTASK_STATUS=(
    (0,'初始'),
    (1,'已经拨打'),
)

class CallTask(models.Model):
    src_uid = models.CharField('拨打用户',max_length=30)
    dst_uid = JsonAbleField('接收用户',)
    call_time = models.DateTimeField('拨打时间')
    tone_list = JsonAbleField('拨打内容',blank=True,default=[])
    status = models.IntegerField('状态',blank=True,default=0,choices=CALLTASK_STATUS)
    