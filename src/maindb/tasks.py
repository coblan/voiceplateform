from settings.celery import app
import requests
import urllib
from django.conf import settings
import json
from maindb.models import CallRecord
from part3.rabbit_instance import robot_receive_call
import logging
general_log = logging.getLogger('general_log')

@app.task
def channel_reject_monitor(uid,channel):
    url = urllib.parse.urljoin(settings.APP_HOST,'/extphone_new/ext/setting/call')
    rt = requests.post(url,data= json.dumps( {'userNo':uid} ) )
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
    
    