from helpers.director.shortcut import director_view,doc_fun,doc_str
from django.conf import settings
import time
from . Agora.RtcTokenBuilder import RtcTokenBuilder
from . Agora.RtmTokenBuilder import RtmTokenBuilder

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
[GET]   /dapi/agora/rtm-option?channel=mychanel&uid=1235          

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