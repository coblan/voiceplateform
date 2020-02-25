from helpers.director.shortcut import director_view
from django.conf import settings
import time
from . Agora.RtcTokenBuilder import RtcTokenBuilder
from . Agora.RtmTokenBuilder import RtmTokenBuilder
from . rabbit_instance import send_msg,send_mp3,notify_quit_robot,robot_receive_call,robot_call_user
from helpers.func.random_str import get_str
from maindb.models import Accountinfo,VoiceMsgList,CallRecord
from .apple.apns import VoiceCallPush
from django.utils import timezone
from helpers.director.model_func.dictfy import sim_dict
from helpers.director.network import argument
import json
from helpers.func.sim_signal import sim_signal
import logging
general_log = logging.getLogger('general_log')


'''{"doc":'api/call.md','sort':50}
### 拨打序列图

``` mermaid::

    sequenceDiagram
    participant RTC
    participant A as 拨打方A
    participant  B as 被叫方B
    participant  S as 服务器
    
    A->>S:请求通知B
    activate A
    S-->>A:返回token
    A->>RTC:加入频道
    deactivate A
    S-->>B:消息通知B
    activate B
    B-->>S:启动app时请求是否有被叫消息
    B->>S:申请接听频道
    S-->>B:返回token
    deactivate B
    B->>RTC:加入频道
    A->B:开始通话
    A->>S:通知服务器通话完结
    A->>RTC:离开频道
    B->>S:通知服务器通话完结
    B->>RTC:离开频道
    

```
'''

@director_view('call/user')
def call_user(src_uid,dst_uid =None,extra_msg=''):
    '''{'doc':'api/call.md',}
    ### 拨打
    用户拨打电话给其他人
    
    @dst_uid:list
    '''
    if isinstance(dst_uid,str):
        dst_uid = dst_uid.split(',')
            
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName= 'ch_'+ get_str(length=10)
    userAccount= src_uid
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    general_log.info('[%s]向[%s]拨打语音'%(src_uid,dst_uid))
    #VoiceMsgList.objects.create(uid = src_uid,channel=channelName,status=1,extra_msg=extra_msg)
    sim_signal.send('call.call',uid=src_uid,channel=channelName,src_uid=src_uid,dst_uid=dst_uid,extra_msg=extra_msg,is_robot=False)
    if dst_uid:
        for uid in dst_uid:
            sim_signal.send('call.call',uid=uid,channel=channelName,src_uid=src_uid,dst_uid=dst_uid,extra_msg=extra_msg)
            #VoiceMsgList.objects.create(uid = uid,channel=channelName,extra_msg=extra_msg)
        
        users = Accountinfo.objects.filter(uid__in = dst_uid).exclude(apns_token="")
        for user in users:
            infodc = {
                'title':'audiocall',
                'accountCaller':src_uid,
                'channel':channelName,
            }
            VoiceCallPush(user.apns_token, infodc,src_user = src_uid).push()
    
    return {
        'appID':appID,
        'channel':channelName,
        'uid': userAccount,
        'token':token,
    }

#@director_view('call/end')
#def end_call(uid,channel):
    #'''{'doc':'api/call.md',}
    #### 结束拨打
    #当用户挂断电话时，SDK通知后台，后台会更新用户的语音消息状态。
    #```
    #[POST]    /dapi/call/end
    #参数:
    #{
        #uid:'12355', # 用户ID ,必填
        #channel:"ch_12356f34", # 频道名称，必填
    #}
    #返回:
    #{
    #}
    #```
    #'''
    #sim_signal.send('call.quit',uid=uid,channel=channel)
    ##VoiceMsgList.objects.filter(uid = uid,channel=channel).update(status=2)
    #general_log.debug('[%(uid)s]结束[%(channel)s]通话'%locals() )

@director_view('call/msg')
def get_voice_msg(uid):
    '''{"doc":"api/user.md"}
    ### 获取用户的最近语音消息
    
    最近2分钟内的语音消息
    '''
    now = timezone.now()
    rows = []
    for item in VoiceMsgList.objects.filter(uid = uid,status=0,createtime__gte = (now- timezone.timedelta(minutes=2) )):
        rows.append(sim_dict(item))
    return rows

@director_view('call/token')
def recieve(uid,channel):
    '''{"doc":"api/call.md"}
    ### 接收频道
    SDK接听电话时，获取token。
    ```
    [POST]    /dapi/call/enter
    参数
    {
        uid:'12343',# 用户uid，必填
        channel:'ch_234werrty', # 频道，必填
    }
    ```
    '''
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName= channel
    userAccount= uid
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    
    general_log.debug('[%(uid)s]接听[%(channel)s]通话'%locals() )
    #sim_signal.send('call.enter',uid,channel)
    return {
        'appID':appID,
        'channel':channelName,
        'uid': userAccount,
        'token':token,
    }

@director_view('invite/robot')
def invite_robot(uid,channel):
    '''{"doc":"api/call.md"}
    ### 要求机器人接入
    拒绝接听时，要求机器人接入
    ```
    [POST]    /dapi/invite/robot
    参数:
    {
        uid:'12355',# 用户uid，字符串，必填
        channel:'ch_23243536' , # 频道，必填
    }
    ```
    '''
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName= channel
    userAccount= uid
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    
    # 根据当前需求，后台只需要推送 from to 给机器人，由机器人自己到 app后台去拿mp3数据
    record = CallRecord.objects.get(channel = channelName)
    robot_receive_call(src=record.src_uid, dst=uid, token=token, appid=appID, channel=channelName)
    #userinfo = Accountinfo.objects.filter(uid=uid).first()
    #if userinfo and userinfo.reject_tone:
        #send_mp3(channel,tone_list=json.loads(userinfo.reject_tone),src_uid= uid)
    #else:
        #send_mp3(channel,tone_list=[{'url':'/static/reject_tone.mp3','before_second':0},],src_uid= uid)
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
    '''{"doc":"agora/early_test.md"}
    ### 直接拨打机器
    直接拨打机器人，演示用
    废弃[2020/2/12]
    '''
   
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


@director_view('quit/robot')
def quit_robot(channel,uid=None):
    '''{"doc":"api/call.md"}
    ### 踢出机器人
    踢出机器人
    ```
    [POST]    /dapi/quit/robot
    参数:
    {
        channel:"ch_xwerewwt", # 频道，必填
    }
    ```
    '''
    general_log.debug('发送消息退出频道[%s]'%channel)
    notify_quit_robot(channel,uid)

    
'''{"doc":"agora/early_test.md"}
# 语音对接
全部是测试用，正式应该无用
### 声网接口

[Python 生成token](https://docs-preview.agoralab.co/cn/Audio%20Broadcast/token_server_python?platform=Python)

'''

@director_view('agora/token')
def get_token():
    '''{"doc":"agora/early_test.mdd"}
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

@director_view('agora/rtc-option')
def get_option(uid=None,channel=None,):
    '''{"doc":"agora/api.md"}
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


@director_view('agora/rtm-option')
def get_option(uid=None,channel=None,):
    '''{"doc":"agora/api.md"}
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
    "/rtc 页面会调用"
    send_mp3(channel, mp3_url)