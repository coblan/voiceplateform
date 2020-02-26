from helpers.maintenance.log.elk import ELKHander
from django.conf import settings
import json
import os

class RTCLOG(ELKHander):
    host = settings.ELK.get('host')
    user = settings.ELK.get('user')
    pswd = settings.ELK.get('pswd')
    index = settings.ELK.get('voice_rtm_msg')
    
    def clean_hostname(self,msg):
        dc = json.loads(msg)
        return {
            'msg':dc.get('msg'),
            'hostname':'%s-[%s]'%(self.hostName,dc.get('proc_name')),
        }
    

class VoiceplatformLOG(ELKHander):
    host = settings.ELK.get('host')
    user = settings.ELK.get('user')
    pswd = settings.ELK.get('pswd')
    index = settings.ELK.get('voiceplatform') 
    
    def clean_hostname(self,msg):
        EXTRA_HOST = os.environ.get('EXTRA_HOST')
        if EXTRA_HOST:
            return {
                'msg':msg,
                'hostname':'%s-[%s]'%( self.hostName ,EXTRA_HOST)
            }
        else:
            return {
                'msg':msg,
                'hostname':self.hostName
            }