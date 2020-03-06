from settings.celery import app
import requests
import urllib
from django.conf import settings
import json
from maindb.models import CallRecord,CallEvent
from part3.rabbit_instance import robot_receive_call
import subprocess
from helpers.func.random_str import get_random_number
from part3.Agora_interface import get_rtc_option
import os
from helpers.director.model_func.dictfy import sim_dict
from helpers.director.kv import get_json

import logging
general_log = logging.getLogger('general_log')

@app.task
def channel_reject_monitor(uid,channel):
    url = urllib.parse.urljoin(settings.APP_HOST,'/extphone_new/ext/setting/call')
    rt = requests.post(url,json= {'userNo':uid}  )
    general_log.info('请求app服务器[%s] %s的拒接等待时间 ,返回结果 %s'% (url,uid,rt.text) )
    waittime= 0 #settings.REJECT_WATI
    if rt.status_code==200 and rt.json().get('code') ==1 and  rt.json().get('data').get('data').get('isAutoAnswer'):
        waittime = rt.json().get('data').get('data').get('waitTime',waittime)
    if waittime:
        general_log.debug(' %s 秒后检查 频道=%s 是否接听'% (waittime,channel) )
        check_is_receive.apply_async(args=(channel,),countdown=waittime)
    else:
        general_log.debug(' 用户=%s 没有拒接等待时间 '% uid )

@app.task
def check_is_receive(channel):
    general_log.debug('延时任务，检查频道=%s是否有人接听'% channel )
    call = CallRecord.objects.get(channel = channel)
    if not call.starttime:
        general_log.info('%s 过期未接听，现在机器人接入'%channel)
        robot_receive_call(call.src_uid,call.dst_uid[0],call.channel)

@app.task
def recording(channel):
    #ss = './recorder_local --appId 303156d224e44881a00af9cabc9e10d8 --channel haha --uid 2245 --channelKey 006303156d224e44881a00af9cabc9e10d8IACHQjxBpV/8289VBT0fRQgzIy7QR8/QC4SwTfMpMiGMZYYRUgEc6RCxEADQkdcEJA9UXgEAAQD8v1Je  --appliteDir ~/agoracore/Agora_Recording_SDK_for_Linux_FULL/bin --lowUdpPort 14000 --highUdpPort 15000'
    general_log.info('开始录音，频道为%s'%channel)
    
    uid = get_random_number(5)
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
        'idle':settings.RECORD.get('idle',3),
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
    --isMixingEnabled 1 \
    --idle %(idle)s\
   '''
    order = order % dc
    general_log.debug('录制命令:%s'%order)
    
    subprocess.Popen(order,shell=True,executable='/bin/bash')
    #os.system(order)
    
    #f=open("/dev/null",'r')
    #Popen(order,shell=True,stdout=f,executable='/bin/bash')
    #f.close
    #os.system(order)
    
@app.task
def push_callrecord(channel):
    record = CallRecord.objects.get(channel=channel)
    url = get_json('cfg_push_call_record')
    if url:
        dc = sim_dict(record)
        event = []
        resource ={
            'captions':[],
            'recording':[],
            'recording_timestamp':[],
        }
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
            resource['captions'].append(caption_dc)
        
        path = os.path.join( settings.RECORD.get('tone_dir'),record.channel)
        if os.path.exists(path):
            for fl in os.listdir(path):
                fl_url = urllib.parse.urljoin(settings.RECORD.get('tone_url'),fl)
                if fl.endswith('.aac') :
                    resource['recording'].append(
                        {'userid':0,'kind_label':'录音','content':fl_url,}
                    )
                elif fl.endswith('.txt') and fl.startswith('uid_'):
                    resource['recording_timestamp'].append(
                        {'userid':0,'kind_label':'录音时间戳','content':fl_url}
                    )
                    
        # 临时决定，只取第一个
        resource['recording'] =  resource ['recording'][:1]
        resource['recording_timestamp'] =  resource ['recording_timestamp'][:1]
        
        dc['resource'] = resource
        general_log.debug('推送数据:%s'%json.dumps(   {'callrecord':dc}   ) )
        
        rt = requests.post(url,json= {'callrecord':dc})
        
        general_log.info('推送拨打记录给app后台,返回状态码%s,返回结果%s'%(rt.status_code,rt.text))
        
    else:
        general_log.info('推送拨打记录给app后台，但是没有设置推送地址!')