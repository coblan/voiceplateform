from helpers.func.sim_signal import sim_signal
from .models import VoiceMsgList,CallRecord,CallEvent
from django.db.models import F
import json
from django.utils import timezone
import requests
from helpers.director.kv import get_json
from helpers.director.model_func.dictfy import sim_dict
import logging
general_log = logging.getLogger('general_log')

@sim_signal.recieve('call.call')
def call_call(uid,channel,src_uid=None,dst_uid=None,extra_msg=None,is_robot=False):
    VoiceMsgList.objects.create(uid = uid,channel=channel,status=0,extra_msg = extra_msg )
    obj,created = CallRecord.objects.get_or_create(src_uid=src_uid,dst_uid=dst_uid,channel = channel,is_robot=is_robot)
    if created:
        CallEvent.objects.filter(channel=channel).update(record=obj)
    

@sim_signal.recieve('call.enter')
def call_start(uid,channel):
    VoiceMsgList.objects.filter(uid = uid,channel=channel).update(status=1)
    CallRecord.objects.filter(channel=channel).update(count = F('count')+1 )
    record  =CallRecord.objects.get(channel = channel)
    if not record.starttime:
        record.starttime = timezone.now()
    record.save()

@sim_signal.recieve('call.quit')
def call_quit(uid,channel):
    VoiceMsgList.objects.filter(uid = uid,channel=channel).update(status=2)
    CallRecord.objects.filter(channel =channel).update(count = F('count')-1)
    record = CallRecord.objects.get(channel = channel)
    if record.count <=0:
        record.endtime = timezone.now()
        record.save()
        sim_signal.send('call.end',record)

@sim_signal.recieve('call.end')
def call_end(record):
    url = get_json('cfg_push_call_record')
    if url:
        dc = sim_dict(record)
        event = []
        for item in record.callevent_set.all():
            item_dc = sim_dict(item)
            for k,v in dict(item_dc).items():
                if k.startswith('_'):
                    item_dc.pop(k)
            event.append(item_dc)
        dc['event'] = event
        rt = requests.post(url,json= {'callrecord':dc})
        
        general_log.info('推送拨打记录给客户,返回状态码%s,返回结果%s'%(rt.status_code,rt.text))
        
    else:
        general_log.info('推送拨打记录给客户，但是没有设置推送地址!')

