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