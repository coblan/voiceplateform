from helpers.pcweb.shotcut import web_page_dc

class RTCSendPage(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_label(self):
        return 'rtc发送页面'
    
    def get_context(self):
        rtc_send=[]
        for i in range(30):
            rtc_send.append( {'editor':'com-rtc-send'})
            
        return {
            'tops':[
                {'editor':'com-rtc-trigger'},
                *rtc_send,
                #{'editor':'com-rtc-send'},
                #{'editor':'com-rtc-send'},
                #{'editor':'com-rtc-send'},
            ]
        }
    
web_page_dc.update({
    'rtc-send':RTCSendPage
})