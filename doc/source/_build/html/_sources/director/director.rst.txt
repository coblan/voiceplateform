登录
==========

原始登录方式
-------------
::

    /dapi/do_login     POST

    参数:
    {"username":"xx","password":"xxx"}

    返回:
    {
        "data": {
            "token": "i7u62v4o5340950xt3jguyilxgmodvxp",
            "success": true
        },
        "success": true
    }

调用登录接口后，有两种方式与后台交互。

1.直接用cookies
    后台已经自动设置和http请求的cookies，如果携带cookies请求，可以直接请求其他api接口。

2. 采用token
   如果传递cookies有困难，直接将token放在http的header中，进行请求 字段名为 :code:`Authorization:token`

3. 直接挂在url上请求，例如 : api_url?token=xxx

.. Note:: 在浏览器中肯会存在跨域问题。后端进行了设置是允许跨域请求的，但是浏览器默认是不允许传递cookies等敏感信息，所以需要进行一定的设置。

以jquery的请求为例,需要设置 :code:`withCredentials: true`

::

    $.ajax({
        url: a_cross_domain_url,
        xhrFields: {
            withCredentials: true
        }
    });


device code登录
----------------------
将device_code挂接在url后面，进行api请求。
::

    /dapi/aaaa?device_code=12345

后台会自动生成一个对应的用户，其用户名为 device_code ,并让该用户登录