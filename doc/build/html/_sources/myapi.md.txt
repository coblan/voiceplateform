# API

### 上传用户

```
/dapi/account/update           POST
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

### 用户拨打
```
/dapi/call/user               POST
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

