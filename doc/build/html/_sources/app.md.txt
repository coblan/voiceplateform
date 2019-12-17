app版本控制
==============
当前版本需要在后台进行设置

![Image](./_static/app_version.png)

## 前端请求接口
### hot热更新
判断当前版本是否需要热更新!

```
/dapi/checkupdate/hot?version=1
@version:用户的app版本

 返回:

{
    "success": true,
    "data": {
        "needupdate": false,
        "latest_version":123,
    }
}
```



``` note:: 当测试开关打开时，只有在测试名单里面的用户才会被通知热更新。
```


### app更新

服务器最新app版本。

```
/dapi/checkupdate/app?version=1

返回:
{
    "success": true,
    "data": {
        "needupdate": true,
        "path": "ssss" // app下载路径
    }
}
```

### app资源地址中转

服务器做了一个中转地址接口，使用方式如下

在后台app更新*管理界面*填写资源真实的域名 `http://www.resourece.com`。假设后台域名为 http://color.kingstorming.com 利用 http://color.kingstorming.com/res/resource_real_path 来进行请求， 后台会重定向到 http://www.resourece.com/resource_real_path