# 代码及部署

`拨打后台`采用python+django进行开发。后台管理界面主要使用`vue.js`进行开发。

现在开发测试环境使用 Ubuntu18.04 + Python3.6+django1.11  

管理后台界面vuejs 版本2.6.10


webserver 建议采用 nginx + uwsgi 形式

数据库建议使用 mysql5.7

测试环境消息队列:rabbitmq ,版本 3.6.10

日志系统建议采用 elk 7.1