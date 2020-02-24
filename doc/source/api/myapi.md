# 拨打

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

### 用户拨打
用户向其他用户拨打电话，可以是向一个用户也可以向多个用户拨打
```
[POST]  /dapi/call/user       

参数示例
{
    src_uid:"12356",
    dst_uid:["12345","34566"],
    extra_msg:"your extra message"
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|src_uid   | 自己的uid，用于签名token | 是   |
| dst_uid   | 对方的uid数组 ，如果对方是苹果用户，会push消息给对方 |  否 |
| extra_msg  | 额外信息(客户端请求语音信息时，该信息会传递给客户端) | 否 |

返回 
```
{
    "success": true,
    "data": {
        "appID": "303156d224e44881a00af9cabc9e10d8",
        "channel": "ch_4aY875LP4o",
        "uid": "1234",
        "token": "006303156d224e44881a00af9cabc9e10d8IACgUJJitrMNSv8lt51GOztehgjZLfpgtuWC6mDDhAKBeJMxVymj4OObEADw9+kBR7MUXgEAAQAfZBNe"
    }
}
```

### 直接拨打机器人
*该接口用于演示目的*,客户端拿到返回的`channel`后，就加入该频道，后台机器人会在该频道播放预先准备好的音频。

```
[POST]  /dapi/call/robot
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|src_uid   | 自己的uid，用于签名token | 是   |

返回
```
{
    "success": true,
    "data": {
        "appID": "303156d224e44881a00af9cabc9e10d8",
        "channel": "ch_b5O729YA23",
        "uid": "12345",
        "token": "006303156d224e44881a00af9cabc9e10d8IADayEfx+2LpKe++OZ08xiOyOY1xAE4y0cLFagSx6DXQr6I35iUcOvXLEABnbngE/uwVXgEAAQDWnRRe"
    }
}
```

<!-- ### 获取token

被叫用户加入频道需要token，调用该接口获取token

```
[POST]  /dapi/channel/join

{
    "uid":"1234",
    "channel":"ch_xergsde"
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|uid   | 用户的uid | 是   |
|channel   | 频道名 | 是   |

返回
```
{
    "success": true,
    "data": {
        "appID": "303156d224e44881a00af9cabc9e10d8",
        "channel": "ch_xergsde",
        "uid": "1234",
        "token": "006303156d224e44881a00af9cabc9e10d8IAAcLnRJAGjM7DIH6qEO4Ef8j8h3NNMDxj8xpSjblZ9SXR6ERHqj4OObEABa+9gDky4XXgEAAQBr3xVe"
    }
}
``` -->

### 最近通话消息

返回最近(`暂定1分钟`)的拨打消息。主要作用是:

* 当app启动时，需要调用一下该接口，客户端可以以此判断否有人给自己拨打语音电话。
* 任意拨打方可以调用该接口,查询自己最近是否有通话会话，以此辅助判断自己是否断线。


```
[POST]  /dapi/call/msg

示例参数:
{
    'uid':'4321'
    }
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|uid   | 用户的uid | 是   |

返回
```
{
    'success': True, 
    'data': [
        {'id': 16, 
        'uid': 4321, 
        'channel': 'ch_iX48Sle954',
         'status': 0, 
         '_status_label': '初始化',
          'createtime': '2020-01-10 00:19:40', 
          'pk': 16,
          'extra_msg':'caller send extra message'}]
    }

```
返回的状态值status

|  值    |   含义        | 
|----------| ---------------|
|0   | 初始化 | 
|1   | 信息已获取 | 
|2   | 通话已经完结 | 

当客户端退出频道时，必须通知服务器，以维持该状态值的准确性。

### 进入频道token

任何用户频道通话时，通过该接口获取app token信息

```
[POST]  /dapi/call/token

示例参数:
{
    'uid':'4321',
    'channel':'ch_sdgsdgsgs',
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|uid   | 用户的uid | 是   |
|channel   | 频道 | 是   |

返回
```
{'success': True, 
'data': {
    'appID': '303156d224e44881a00af9cabc9e10d8', 
    'channel': 'ch_04g1j0531W', 
    'uid': '4321', 
    'token': '006303156d224e44881a00af9cabc9e10d8IADUmLAwn3zGNLGaIIyrz6M4I1rJ0/Sx0+9uP+mChtxlVaHThWxov47EEAAqbGEE+KUYXgEAAQDQVhde'
    }
}

```


### 通话事件上报

```
[POST]  /dapi/call/event

参数{
    "uid":"12345",
    "channel":"ch_1235",
    "code":1, 
    "desp":"接通",
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|uid   | 用户的uid | 是   |
|channel   | 频道 | 是   |
| code | 事件编码| 是|
| desp | 详细描述    | 否 |


事件code具体描述:

| Code | 描述 |
|------|------|
| 1   |  开始通话 （指通话有2人或是多人进入通话）|
| 2   | 通话结束 (在通话过程中结束通话，未进入通话前的拨号结束不是该事件) |
| 1000 | 发起方事件：通话方取消通话，通话方发起通话，在通话在响铃未接通时通话方取消通话 |
| 1001  | 发起方事件：通话方发起通话，无人接听，超时结束通话 |
| 1002  | 发起方事件：通话方发起通话，接听方拒接电话，通话结束 |
| 1003 | 接听方事件：接听方拒接电话，通话结束 |
| 1006 | 接听方事件：通话方取消通话，通话结束 |
| 1007 | 通用事件：通话中遇到错误，通话失败，通话结束 |


### 请求机器人进入频道
当用户拒接电话时，可以请求机器人接入该频道

```
[POST]  /dapi/invite/robot

示例参数:
{
 "uid":"1235",
'channel':'ch_sdgsdgsgwe'
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|uid   | 用户的uid | 是   |
|channel   | 频道 | 是   |

返回
```
{
    "success": true,
    "data": {
        "appID": "303156d224e44881a00af9cabc9e10d8",
        "channel": "ch_sdgsdgsgwe",
        "uid": "1235",
        "token": "006303156d224e44881a00af9cabc9e10d8IADcxCL86Hiy0kAF/mKUdbNh2lBGVH+RQ+GAXMwinkoZjwEAybM10OTsEABu3lAAHhwcXgEAAQD2zBpe"
    }
}
```

### 将机器人踢出频道

```
[POST]  /dapi/quit/robot

示例参数
{
    "channel":"ch_dgfd2et123",
    "uid":"1235",
    }
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|channel   | 频道 | 是   |
| uid | 请求的用户ID | 是 |

返回
```
{
    "success": true,
    "data": null
}
```

### 定时拨打电话

定时拨打需要更新拨打信息

#### 上传拨打信息
```
[POST]  /dapi/calltask/update

参数
{
    'id':'',
    'src_uid':'1234',
    'dst_uid':['1235','1236'],
    'call_time':'2020-02-02 20:20:00',
    'taskid':'123',
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|id   | 数据库唯一标识，如果有值则是更新数据，如果无值则插入新的数据 | 否   |
| src_uid | 发起用户   | 是 |
| dst_uid  | 接收用户列表   | 是  |
|call_time  | 拨打时间，注意时间格式  | 是 |
| taskid | app后台对应的任务ID | 是 |


#### 获取拨打列表
```
[POST]  /dapi/calltask/list
参数示例
{
    'uid':'1234'
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|uid   | 用户id | 是   |

返回:
```
{
    'success': True, 
    'data': {
        'rows': [
            {'id': 8, 
            'src_uid': '1234', 
            'dst_uid': ['1235', '1236'], 
            'call_time': '2020-02-02 20:20:00', 
            'tone_list':[],
            'pk': 8}], 
            'row_pages': {
                'crt_page': 1, 
                'total': 1, 
                'perpage': 20
                }
        }
}

```

### 心跳检查通话

当处在某个频道通话时，客户端需要每隔30内通知一次后台，否则后台可能会判断客户端已经掉线。

```
[POST]  /dapi/call/heartbeat
参数
{
    uid:'1234',
    channel:'cha_235',
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|uid   | 用户id | 是   |
| channel | 频道名称 | 是 |



