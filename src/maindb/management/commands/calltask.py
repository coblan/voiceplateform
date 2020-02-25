
from django.core.management.base import BaseCommand
from django.conf import settings
from helpers.director.base_data import director
from django.utils import timezone
from helpers.func.random_str import get_str
from part3.apple.apns import VoiceCallPush
from maindb.models import CallTask,Accountinfo
from part3. rabbit_instance import send_msg,send_mp3,robot_call_user
import json
from helpers.func.sim_signal import sim_signal

import logging
general_log = logging.getLogger('general_log')

class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):
        now = timezone.now()
        general_log.debug('启动定时拨打任务')
        for task in CallTask.objects.filter(status = 0,call_time__lte= now):
            #general_log.debug('定时拨打src_uid=%s;dst_uid=%s'%(task.src_uid,task.dst_uid))
            task.status = 1
            task.save()
            general_log.info('机器人拨打任务 %s'% task.pk )
            call_user(task.src_uid,task.dst_uid,task.taskid)
            
        general_log.debug('定时拨打任务结束')
    
def call_user(src_uid,dst_uid,taskid):
    '''
    机器人主动拨打电话给用户
    @dst_uid:list
    '''
    #appID = settings.AGORA.get('appID')
    #appCertificate = settings.AGORA.get('appCertificate')
    channelName= 'ch_'+ get_str(length=10)
    #userAccount= src_uid
    #Role_Attendee = 2
    #privilegeExpiredTs = time.time() + 600
    #token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    
    #VoiceMsgList.objects.create(uid = src_uid,channel=channelName,status=1,extra_msg=extra_msg)
    
    
    #send_mp3(channelName, tone_list,src_uid)
    # 当前不需要推送mp3到前台，机器人自己去app后台拿
    robot_call_user(src_uid, dst_list = dst_uid, channel_name =channelName,taskid=taskid)
    if dst_uid:
        for uid in dst_uid:
            #VoiceMsgList.objects.create(uid = uid,channel=channelName,extra_msg=extra_msg)
            extra_msg_dc ={
                'Subscribers':dst_uid,
                'CallerId':src_uid,
                'Type':1,
                'robot':True
            }
            extra_msg = json.dumps(extra_msg_dc,ensure_ascii=False)
        
            sim_signal.send('call.call',uid = uid,channel=channelName,src_uid=src_uid,dst_uid=dst_uid,extra_msg=extra_msg,is_robot=True)
            
            dc = {
                "title" : "audiocall",
                "accountCaller" : src_uid,
                "channel" : channelName,
                "accountRemote" : uid,
              }
            if len(dst_uid) >=1:
                dc['extra_msg']= dst_uid
            send_msg(json.dumps(dc,ensure_ascii=False), uid)
        
        users = Accountinfo.objects.filter(uid__in = dst_uid).exclude(apns_token="")
        for user in users:
            infodc = {
                'title':'audiocall',
                'accountCaller':src_uid,
                'channel':channelName,
            }
            VoiceCallPush(user.apns_token, infodc,src_user = src_uid).push()
           
    
    #return {
        #'appID':appID,
        #'channel':channelName,
        #'uid': userAccount,
        #'token':token,
    #}