# 声网接口

### 获取token
可能没有什么用，暂时放这里
```
[GET]       /dapi/agora/token               
```

### 获取option

根据声网接口文档，需要用到`appID,channel,uid,token`这些参数，现在可以由后端直接生成，返回给前端使用。
``` note:: 当前用户是写死的，等待用户系统的确定
```
```
[GET]      /dapi/agora/rtc-option          

```
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