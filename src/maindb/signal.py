from helpers.func.sim_signal import sim_signal
from .models import VoiceMsgList,CallRecord,CallEvent
from django.db.models import F
import json
from django.utils import timezone

@sim_signal.recieve('call.call')
def call_call(uid,channel,src_uid=None,dst_uid=None,extra_msg=None,is_robot=False):
    VoiceMsgList.objects.create(uid = uid,channel=channel,status=0,extra_msg = extra_msg )
    obj = CallRecord.objects.get_or_create(src_uid=src_uid,dst_uid=dst_uid,channel = channel,is_robot=is_robot)
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
    pass
    

