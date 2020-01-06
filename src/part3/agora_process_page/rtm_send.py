from helpers.pcweb.shotcut import web_page_dc
from django.conf import settings

class RTMSendPage(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_label(self):
        return 'rtm发送页面'
    
    def get_context(self):
        return {
            'tops':[
                {'editor':'com-rtm-send'},
            ]
        }
    
web_page_dc.update({
    'rtm-send':RTMSendPage
})