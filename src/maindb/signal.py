from helpers.func.sim_signal import sim_signal
from .models import VoiceMsgList
import json

@sim_signal.recieve('call.start')
def call_start(uid,channel,src_uid=None,dst_uid=None,extra_msg=None):
    if not extra_msg:
        extra_msg_dc ={
            'Subscribers':dst_uid,
            'CallerId':src_uid,
            'Type':1,
            'robot':True
        }
        extra_msg = json.dumps(extra_msg_dc,ensure_ascii=False)
    
    VoiceMsgList.objects.create(uid = uid,channel=channel,extra_msg = extra_msg )

