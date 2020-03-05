# 其他接口


```eval_rst
.. _upload:
```
## 文件上传

```
[POST]  /d/upload
```
参数名字随意，如果是单个文件，返回的一个url，如果是同时上传多个文件返回的是一个相同数量的数组

返回
```
[
    "/media/general_upload/0a2533c28a18ac79057a93b5817da886.jpg"
]
```

## 系统设置

```
[GET]  /dapi/system/config
```

返回:

```
{
    "success": true,
    "data": {
        "channel_heartbeat": 30，// 频道心跳间隔
        "agora_appid":"12312432435", // appid
    }
}
```

## 外部系统

客户如果需要同步通话记录，可以在后台设置回调API地址。每当通话结束时，后台会向这个回调地址发送通话记录数据。

1. 在后台配置推送地址。该地址的接口API，应该能够接受POST请求,json格式。
2. 后台在通话结束时，如果配置了回调api地址，会向该api推送该条通话记录。

推送的通话记录数据结构如下。

```
{
    'callrecord':{
        'channel': 'ch_56Cm7p82K5',  // 通话频道
        'dst_uid': ['511'],  // 被叫用户uid
        'id': 12,  // 通话记录id
        'is_robot': False,  // 是否机器人主动拨打
        'src_uid': '515',   // 拨打用户uid
        'starttime': '2020-02-12 21:02:27'   // 通话开始时间
        'endtime': '2020-02-12 21:026:27',   // 通话结束时间
        'event': [{'channel': 'ch_56Cm7p82K5',  // 通话频道
                    'code': 102,   // 时间编码
                    'createtime': '2020-02-14 21:02:27',  // 事件发生时间
                    'desp': '3',   // 事件详细描述
                    'id': 7,   // 事件ID
                    'sender_typ':0, // 普通用户上报
                    'pk': 7,
                    'record': 12,  // 事件对应的通话记录ID
                    'uid': 515},   // 事件上报用户uid
                {'channel': 'ch_56Cm7p82K5',
                    'code': 103,
                    'createtime': '2020-02-14 21:02:27',
                    'desp': '',
                    'id': 8,
                    'sender_type':1, // 机器人上报
                    'pk': 8,
                    'record': 12,
                    'uid': 511}],
        'resource':{
            "captions":[
                {user:'1231',kind_label:'字幕',content:'深深深算宫灯'start:'2020-10-01 10:20:20',end:'2020-10-01 10:23:20',},
            ],
            "recording":[
                {user:'1231',kind_label:'录音',content:'/media/ssg/12342.acc'},
            ],
            "recording_timestamp":[
                {user:'1231',kind_label:'录音时间戳',content:'/media/ssg/12342.text'},
                {user:'1231',kind_label:'录音时间戳',content:'/media/ssg/12342_02.text'},
                {user:'1231',kind_label:'录音时间戳',content:'/media/ssg/12342_3.text'},
            ]
        }
            
        ],

        'pk': 12,
        'count': 0,  
        'refreshtime': '2020-02-14 21:02:27',
        }
}
```

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