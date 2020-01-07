from helpers.maintenance.log.elk import ELKHander
from django.conf import settings

class RTCLOG(ELKHander):
    host = settings.ELK.get('host')
    user = settings.ELK.get('user')
    pswd = settings.ELK.get('pswd')
    index = 'voice_rtm_msg'

class VoiceplatformLOG(ELKHander):
    host = settings.ELK.get('host')
    user = settings.ELK.get('user')
    pswd = settings.ELK.get('pswd')
    index = 'voiceplatform'