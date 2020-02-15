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
        
        'dst_uid': ['511'],
        'id': 12,
        'is_robot': False,
        'src_uid': '515',
        'starttime': '2020-02-12 21:02:27'
        'endtime': '2020-02-12 21:026:27',
        'event': [{'channel': 'ch_56Cm7p82K5',
                    'code': 102,
                    'createtime': '2020-02-14 21:02:27',
                    'desp': '3',
                    'id': 7,
                    'pk': 7,
                    'record': 12,
                    'uid': 515},
                {'channel': 'ch_56Cm7p82K5',
                    'code': 103,
                    'createtime': '2020-02-14 21:02:27',
                    'desp': '',
                    'id': 8,
                    'pk': 8,
                    'record': 12,
                    'uid': 511}],

        'pk': 12,
        'count': 0,  
        'refreshtime': '2020-02-14 21:02:27',
        }
}
```
