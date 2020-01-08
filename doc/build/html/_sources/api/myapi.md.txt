# 拨打

### 用户拨打
单对单拨打
```
[POST]  /dapi/call/user               
```

|  参数     |   含义        | 必填 |
|----------| ---------------|-------|
|src_uid   | 自己的uid，用于签名token | 是   |
| dst_uid   | 对方的uid ，如果对方是苹果用户，会push消息给对方 |  否 |

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

### 获取token

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
```
