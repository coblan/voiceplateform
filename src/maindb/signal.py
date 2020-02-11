from helpers.func.sim_signal import sim_signal
from .models import VoiceMsgList

@sim_signal.recieve('call.start')
def call_start(uid,channel):
    VoiceMsgList.objects.create(uid = uid,channel=channel)

