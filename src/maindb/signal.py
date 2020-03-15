from helpers.func.sim_signal import sim_signal
from .models import VoiceMsgList,CallRecord,CallEvent
from django.db.models import F
import json
from django.utils import timezone
import requests
from helpers.director.kv import get_json
from helpers.director.model_func.dictfy import sim_dict
import os
from django.conf import settings
import urllib

import logging
general_log = logging.getLogger('general_log')

from .tasks import channel_reject_monitor,recording,push_callrecord

@sim_signal.recieve('call.call')
def call_call(uid,channel,src_uid=None,dst_uid=None,extra_msg=None,is_robot=False):
    VoiceMsgList.objects.create(uid = uid,channel=channel,status=0,extra_msg = extra_msg )
    obj,created = CallRecord.objects.get_or_create(src_uid=src_uid,dst_uid=dst_uid,channel = channel,is_robot=is_robot)
    if created:
        CallEvent.objects.filter(channel=channel).update(record=obj)
    if len(dst_uid)==1 and uid == dst_uid[0]:
        #channel_reject_monitor(uid, channel)
        channel_reject_monitor.delay(uid,channel)
        #channel_reject_monitor.apply_async(args=(uid,channel),countdown = 2)

@sim_signal.recieve('call.enter')
def call_start(uid,channel):
    
    general_log.debug('频道开始%s'%channel)
    VoiceMsgList.objects.filter(uid = uid,channel=channel,status=0).update(status=1)
    CallRecord.objects.filter(channel=channel).update(count = F('count')+1 )
    
    update_count =  CallRecord.objects.filter(channel=channel,starttime__isnull=True).update(starttime = timezone.now())
    if update_count:
        recording.delay(channel)
    #try:
        #record  =CallRecord.objects.get(channel = channel)
        #if not record.starttime:
            #record.starttime = timezone.now()
        #record.save()
    #except CallRecord.DoesNotExist as e:
        #raise UserWarning(str(e))
    

@sim_signal.recieve('call.quit')
def call_quit(uid,channel):
    VoiceMsgList.objects.filter(uid = uid,channel=channel).update(status=2)
    CallRecord.objects.filter(channel =channel).update(count = F('count')-1)
    update_count = CallRecord.objects.filter(channel =channel,count__lte=0,endtime__isnull= True).update(endtime = timezone.now())
    if update_count:
        sim_signal.send('call.end',channel)
        
    #record = CallRecord.objects.get(channel = channel)
    #if record.count <=0:
        #record.endtime = timezone.now()
        #record.save()
        #sim_signal.send('call.end',record)

@sim_signal.recieve('call.end')
def call_end(channel):
    # 为了防止前面的事务未完成，这里等待两秒再去发送
    push_callrecord.apply_async(args=(channel,),countdown = 2 )
    

