from settings.celery import app
import requests
import urllib
from django.conf import settings
import json
from maindb.models import CallRecord
from part3.rabbit_instance import robot_receive_call
import subprocess
from helpers.func.random_str import get_random_number
from part3.Agora_interface import get_rtc_option
import os

import logging
general_log = logging.getLogger('general_log')

@app.task
def channel_reject_monitor(uid,channel):
    url = urllib.parse.urljoin(settings.APP_HOST,'/extphone_new/ext/setting/call')
    rt = requests.post(url,json= {'userNo':uid}  )
    general_log.info('请求app服务器%s的拒接等待时间 ,返回结果 %s'% (uid,rt.text) )
    waittime= settings.REJECT_WATI
    if rt.status_code==200:
        waittime = rt.json().get('data').get('data').get('waitTime')
    check_is_receive.apply_async(args=(channel),countdown=waittime)

@app.task
def check_is_receive(channel):
    call = CallRecord.objects.get(channel = channel)
    if not call.starttime:
        general_log.info('%s 过期未接听，现在机器人接入'%channel)
        robot_receive_call(call.src_uid,call.dst_uid,call.channel)

@app.task
def recording(channel):
    #ss = './recorder_local --appId 303156d224e44881a00af9cabc9e10d8 --channel haha --uid 2245 --channelKey 006303156d224e44881a00af9cabc9e10d8IACHQjxBpV/8289VBT0fRQgzIy7QR8/QC4SwTfMpMiGMZYYRUgEc6RCxEADQkdcEJA9UXgEAAQD8v1Je  --appliteDir ~/agoracore/Agora_Recording_SDK_for_Linux_FULL/bin --lowUdpPort 14000 --highUdpPort 15000'
    general_log.info('开始录音，频道为%s'%channel)
    
    uid = get_random_number(11)
    option = get_rtc_option(uid,channel)
    tone_dir = settings.RECORD.get('tone_dir')
    config_path = os.path.join(tone_dir,'%s_config'%channel)
    tone_path = os.path.join(tone_dir,channel)
    
    with open(config_path,'w',encoding='utf8') as f:
        f.write(json.dumps({"Recording_Dir" : tone_path}))
        
    dc ={
        'uid':uid,
        'channel':channel,
        'appid':option.get('appID'),
        'token':option.get('token'),
        'lowUdpPort':settings.RECORD.get('lowUdpPort'),
        'highUdpPort':settings.RECORD.get('highUdpPort'),
        'recorder_local':settings.RECORD.get('recorder_local'),
        'recording_bin':settings.RECORD.get('recording_bin'),
        'idle':settings.RECORD.get('idle',30),
        'config_path':config_path,
        
    }
    order = ''' %(recorder_local)s \
    --uid %(uid)s \
    --appId %(appid)s \
    --channel %(channel)s \
    --channelKey %(token)s \
    --appliteDir %(recording_bin)s \
    --lowUdpPort %(lowUdpPort)s \
    --highUdpPort %(highUdpPort)s \
    --cfgFilePath %(config_path)s\
    --isAudioOnly 1 \
    --idle %(idle)s\
   '''
    order = order % dc
    general_log.debug('录制命令:%s'%order)
    #subprocess.Popen(order,shell=True,executable='/bin/bash')
    os.system(order)
    
    #f=open("/dev/null",'r')
    #Popen(order,shell=True,stdout=f,executable='/bin/bash')
    #f.close
    #os.system(order)
    
    