from settings.celery import app
import requests
import urllib
from django.conf import settings
import json
from maindb.models import CallRecord
from part3.rabbit_instance import robot_receive_call

@app.task
def channel_reject_monitor(uid,channel):
    url = urllib.parse.urljoin(settings.APP_HOST,'/extphone_new/ext/setting/call')
    rt = requests.post(url,data= json.dumps( {'userNo':uid}) )
    waittime= settings.REJECT_WATI
    if rt.status_code==200:
        waittime = rt.json().get('data').get('data').get('waitTime')
    check_is_receive.apply_async(args=(channel),countdown=waittime)

@app.task
def check_is_receive(channel):
    call = CallRecord.objects.get(channel = channel)
    if not call.starttime:
        robot_receive_call(call.src_uid,call.dst_uid,call.channel)
    
    