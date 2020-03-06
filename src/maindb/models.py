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
    (0,'未接通'),
    (1,'已接通'),
    (2,'已挂断'),
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
    dst_uid = JsonAbleField('接收用户',default=[])
    call_time = models.DateTimeField('拨打时间',null=True,blank=True)
    tone_list = JsonAbleField('拨打内容',blank=True,default=[]) # 移到app后台
    status = models.IntegerField('状态',blank=True,default=0,choices=CALLTASK_STATUS)
    taskid = models.IntegerField('任务id',default=0,help_text='app后台的任务ID')
    
    def __str__(self):
        return '拨打计划%s'%self.pk

class CallRecord(models.Model):
    src_uid = models.CharField('拨打用户',max_length=30)
    dst_uid = JsonAbleField('接收用户',)
    channel = models.CharField('通话频道',max_length=30)
    starttime = models.DateTimeField('开始时间',blank=True,null=True)
    endtime = models.DateTimeField('结束时间',blank=True,null=True)
    refreshtime = models.DateTimeField('心跳刷新时间',blank=True,null=True)
    count = models.IntegerField('人员计数',default=0)
    is_robot = models.BooleanField('是否机器人',default=False)
    
    class Meta:
        indexes = [
            models.Index(fields=['channel',]),
        ]

EVENT_CATEGORY = (
    (0,'用户上报'),
    (1,'机器人上报'),
)
    
class CallEvent(models.Model):
    record = models.ForeignKey(CallRecord,blank=True,null=True)
    uid = models.CharField('相关用户',max_length=30)
    channel = models.CharField('通话频道',max_length=30)
    code = models.IntegerField('事件编码',blank=True,null=True)
    desp = models.TextField('事件描述',blank=True)
    createtime = models.DateTimeField('产生时间',auto_now_add=True)
    sender_type = models.IntegerField('上报类型',default=0,choices=EVENT_CATEGORY)
    
    class Meta:
        indexes = [
            models.Index(fields=['channel',]),
        ]
        

class MockApi(models.Model):
    url = models.CharField('api地址',max_length=200)
    content = models.TextField('返回内容',help_text='json字符串')


class UserRtcMap(models.Model):
    channel = models.CharField('频道名称',max_length= 30)
    uid = models.CharField('用户名称',max_length=30)
    rtcid = models.IntegerField('RTC映射ID')