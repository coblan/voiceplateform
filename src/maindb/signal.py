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

from .tasks import channel_reject_monitor,recording

@sim_signal.recieve('call.call')
def call_call(uid,channel,src_uid=None,dst_uid=None,extra_msg=None,is_robot=False):
    VoiceMsgList.objects.create(uid = uid,channel=channel,status=0,extra_msg = extra_msg )
    obj,created = CallRecord.objects.get_or_create(src_uid=src_uid,dst_uid=dst_uid,channel = channel,is_robot=is_robot)
    if created:
        CallEvent.objects.filter(channel=channel).update(record=obj)
    if len(dst_uid)==1 and uid == dst_uid[0]:
        channel_reject_monitor.delay(uid,channel)

@sim_signal.recieve('call.enter')
def call_start(uid,channel):
    recording.delay(channel)
    general_log.debug('频道开始%s'%channel)
    VoiceMsgList.objects.filter(uid = uid,channel=channel).update(status=1)
    CallRecord.objects.filter(channel=channel).update(count = F('count')+1 )
    try:
        record  =CallRecord.objects.get(channel = channel)
        if not record.starttime:
            record.starttime = timezone.now()
        record.save()
    except CallRecord.DoesNotExist as e:
        raise UserWarning(str(e))
    

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
    if url or True:
        dc = sim_dict(record)
        event = []
        resource =[]
        for item in record.callevent_set.all().exclude(code =3):
            item_dc = sim_dict(item)
            for k,v in dict(item_dc).items():
                if k.startswith('_'):
                    item_dc.pop(k)
            event.append(item_dc)
        dc['event'] = event
        
        for item in record.callevent_set.filter(code=3):
            caption_dc =   {'userid':item.uid,'kind_label':'字幕',}
            caption_dc.update(
                json.loads(item.desp)
            )
            resource.append(caption_dc)
        
        path = os.path.join( settings.RECORD.get('tone_dir'),record.channel)
        if os.path.exists(path):
            for fl in os.listdir(path):
                fl_url = urllib.parse.urljoin(settings.RECORD.get('tone_url'),fl)
                if fl.endswith('.aac'):
                    resource.append(
                        {'userid':0,'kind_label':'录音','content':fl_url,}
                    )
                elif fl.endswith('.txt') and fl.startswith('uid_'):
                    resource.append(
                        {'userid':0,'kind_label':'录音时间戳','content':fl_url}
                    )
                
        dc['resource'] = resource
        rt = requests.post(url,json= {'callrecord':dc})
        
        general_log.info('推送拨打记录给app后台,返回状态码%s,返回结果%s'%(rt.status_code,rt.text))
        
    else:
        general_log.info('推送拨打记录给app后台，但是没有设置推送地址!')

