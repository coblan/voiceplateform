# 用户管理

## 上传用户信息

```
[POST]  /dapi/account/update  
```

| 参数    | 含义    |  必填|
|-------- | ------- | -----|
|uid   | 用户唯一ID | 是   |
|device | 设备类型   | 否   |
| apns_token  |  苹果推送token   | 否 |

返回表示成功
```
{
    "success": true,
    "data": {}
}
```

## 更新用户留言信息
```
[POST]  /dapi/account/reject-tone
参数:
{
    "uid":"12345",
    "tone_list": [
        {"mp3":"/media/userfile/mytone1.mp3"},      // mp3 url
        {"space_second":10000},                     // 间隔时间(秒)
        {"mp3":"/media/userfile/mytone2.mp3"},
        {"space_second":20000},
        {"mp3":"/media/userfile/mytone2.mp3"}
    ]
}
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
| uid    | 用户id           | 是    |
| tone_list | 留言url(如果为空，会清空原来的留言)   | 否  |

前端客户端操作流程

1. 调用 [接口上传](<upload>) 留言音频文件，获得 mp3 url 
2. 调用本接口更新用户留言信息