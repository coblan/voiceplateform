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
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
| uid    | 用户id           | 是    |
| tone_url | 留言url(如果为空，会清空原来的留言)   | 否  |

前端客户端操作流程

1. 调用 [接口上传](<upload>) 留言音频文件，获得tone_url 
2. 调用本接口更新用户留言信息