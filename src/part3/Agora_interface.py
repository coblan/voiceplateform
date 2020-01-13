from helpers.director.shortcut import director_view,doc_fun,doc_str
from django.conf import settings
import time
from . Agora.RtcTokenBuilder import RtcTokenBuilder
from . Agora.RtmTokenBuilder import RtmTokenBuilder
from . rabbit_instance import send_msg,send_mp3,notify_quit_robot
from helpers.func.random_str import get_str
from maindb.models import Accountinfo,VoiceMsgList
from .apple.apns import VoiceCallPush
from django.utils import timezone
from helpers.director.model_func.dictfy import sim_dict
from helpers.director.network import argument
import logging
general_log = logging.getLogger('general_log')

@director_view('call/user')
def call_user(src_uid:int,dst_uid:int =None) -> dict:
    '单个用户拨打另外一个用户'
    
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName= 'ch_'+ get_str(length=10)
    userAccount= src_uid
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    general_log.info('[%s]向[%s]拨打语音'%(src_uid,dst_uid))
    VoiceMsgList.objects.create(uid = src_uid,channel=channelName,status=1)
    
    # 暂时屏蔽
    #if dst_uid:
        #VoiceMsgList.objects.create(uid = dst_uid,channel=channelName)
        
        #user = Accountinfo.objects.filter(uid = dst_uid) .first()
        #if user and user.apns_token:
            #infodc = {
                #'title':'audiocall',
                #'accountCaller':src_uid,
                #'channel':channelName,
            #}
            #VoiceCallPush(user.apns_token, infodc,src_user = src_uid).push()
    
    return {
        'appID':appID,
        'channel':channelName,
        'uid': userAccount,
        'token':token,
    }

@director_view('call/end')
def end_call(uid,channel):
    VoiceMsgList.objects.filter(uid = uid,channel=channel).update(status=2)
    general_log.debug('[%(uid)s]结束[%(channel)s]通话'%locals() )

@director_view('call/msg')
def get_voice_msg(uid):
    now = timezone.now()
    rows = []
    for item in VoiceMsgList.objects.filter(uid = uid,status=0,createtime__gte = (now- timezone.timedelta(minutes=2) )):
        rows.append(sim_dict(item))
    return rows

@director_view('call/recieve')
def recieve(uid,channel):
    '''
    接收频道
    '''
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName= channel
    userAccount= uid
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    
    general_log.debug('[%(uid)s]接听[%(channel)s]通话'%locals() )
    VoiceMsgList.objects.filter(uid = uid,channel=channel,status=0).update(status=1)
    return {
        'appID':appID,
        'channel':channelName,
        'uid': userAccount,
        'token':token,
    }

@director_view('invite/robot')
def invite_robot(uid,channel):
    "拒绝接听时，要求机器人接入"
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName= channel
    userAccount= uid
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    send_mp3(channel,mp3_url='/static/reject_tone.mp3')
    general_log.debug('[%(uid)s]拒绝接听,要求机器人进入[%(channel)s]'%locals() )
    VoiceMsgList.objects.filter(uid = uid,channel=channel).update(status=2)
    
    return {
        'appID':appID,
        'channel':channelName,
        'uid': userAccount,
        'token':token,
    }
    
@director_view('call/robot')
def call_robot(src_uid):
    "演示用"
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName= 'ch_'+ get_str(length=10)
    userAccount= src_uid
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    general_log.info('[%s]向机器人拨打语音'%src_uid)
    
    #send_mp3(channelName,mp3_url='/static/Haydn_Cello_Concerto_D-1.mp3')
    send_mp3(channelName,mp3_url='/static/tts.mp3')
    
    return {
        'appID':appID,
        'channel':channelName,
        'uid': userAccount,
        'token':token,
    }

#@director_view('channel/join')
#def call_robot(uid,channel):
    #"演示用"
    #appID = settings.AGORA.get('appID')
    #appCertificate = settings.AGORA.get('appCertificate')
    #channelName= channel
    #userAccount= uid
    #Role_Attendee = 2
    #privilegeExpiredTs = time.time() + 600
    #token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

    #return {
        #'appID':appID,
        #'channel':channelName,
        #'uid': uid,
        #'token':token,
    #}

@director_view('quit/robot')
def quit_robot(channel):
    general_log.debug('发送消息退出频道[%s]'%channel)
    notify_quit_robot(channel)

    

doc_str('agora/api.md','''
# 语音对接

### 声网接口

[Python 生成token](https://docs-preview.agoralab.co/cn/Audio%20Broadcast/token_server_python?platform=Python)

''')


@doc_fun('agora/api.md',)
@director_view('agora/token')
def get_token():
    '''
### 获取token
可能没有什么用，暂时放这里
```
[GET]   /dapi/agora/token  
```
    '''
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName='test_channel'
    userAccount=987654321
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    return token

@doc_fun('agora/api.md')
@director_view('agora/rtc-option')
def get_option(uid=None,channel=None,):
    '''
### RTC获取token

根据声网接口文档，需要用到`appID,channel,uid,token`这些参数，现在可以由后端直接生成，返回给前端使用。

```
[GET]   /dapi/agora/rtc-option?channel=mychanel&uid=1235          

```

| 参数  | 含义  | 必填  | 默认值  |
|-------|-------|-------|------|
| channel | 频道名称 | 否 | test_channel |
| uid | 用户唯一id | 否 |  987654321 |

返回:
``` javascript
{
    "success": true,
    "data": {
        "appID": "303156d224e44881a00af9cabc9e10d8",
        "channel": "test_channel",
        "uid": 987654321,
        "token": "006303156d224e44881a00af9cabc9e10d8IAAxzfgl2eltoS+/UvNYWOA79m0bgaGryJzew8+iCUUfYY9auH4BAl8BEABxwigBpev5XQEAAQB9nPhd"
    }
}
```
    '''
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName= channel  or 'test_channel'
    userAccount=uid or 987654321
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    return {
        'appID':appID,
        'channel':channelName,
        'uid': userAccount,
        'token':token,
    }


@doc_fun('agora/api.md')
@director_view('agora/rtm-option')
def get_option(uid=None,channel=None,):
    '''
### RTM获取token

根据声网接口文档，需要用到`appID,channel,uid,token`这些参数，现在可以由后端直接生成，返回给前端使用。

```
[GET]   /dapi/agora/rtm-option?uid=1235          

```

| 参数  | 含义  | 必填  | 默认值  |
|-------|-------|-------|------|
| uid | 用户唯一id | 否 |  987654321 |

返回:
``` javascript
{
    "success": true,
    "data": {
        "appID": "303156d224e44881a00af9cabc9e10d8",
        "uid": "987654321",
        "token": "006303156d224e44881a00af9cabc9e10d8IADW2XOcCfXR4zFGhvP+3QhDvarhYrQwgaIaRYHc1jUF2AECXwEAAAAAEACPKcoCMzr7XQEA6AML6/ld"
    }
}
```
    '''
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    #channelName= channel  or 'test_channel'
    userAccount= uid or '987654321'
    Role_Rtm_User = 1
    privilegeExpiredTs = time.time() + 600
    token = RtmTokenBuilder.buildToken(appID, appCertificate, userAccount, Role_Rtm_User, privilegeExpiredTs)
    return {
        'appID':appID,
        #'channel':channelName,
        'uid': userAccount,
        'token':token,
    }

@director_view('celery_send_msg')
def celery_send_msg(msg,uid):
    send_msg(msg, uid)

@director_view('try_send_mp3')
def try_send_mp3(channel,mp3_url):
    send_mp3(channel, mp3_url)