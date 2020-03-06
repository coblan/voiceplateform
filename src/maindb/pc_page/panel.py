from helpers.pcweb.shotcut import web_page_dc
from django.conf import settings

class PanelPage(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_label(self):
        return 'rtc发送页面'
    
    def get_context(self):
            
        return {
            'tops':[
                {'editor':'com-cs-top-pannel','links':[
                    {'label':'管理后台','src':'/pc/callrecord',},
                    {'label':'后台文档','src':'/doc',},
                    {'label':'rabbitmq后台','src':'http://liu.enjoyst.com:10830/','detail':'账号:voice;密码:voice;'},
                    {'label':'elk日志','src':'http://liu.enjoyst.com:10821/','detail':'账号:voice;密码:voice123'},
                    {'label':'rtc模拟','src':'/rtc','detail':'rtc客户端'},
                    {'label':'机器人拨打','src':'/ago/rtc-robot','detail':'机器人测试;录制频道'},
                    
                ]}
            ]
        }
    
web_page_dc.update({
    'p':PanelPage
})