from helpers.pcweb.shotcut import web_page_dc
from django.conf import settings
from helpers.director.shortcut import director_view
from part3.rabbit_instance import robot_call_user,robot_receive_call
from maindb.tasks import recording

class RobotTestPage(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_label(self):
        return '机器人测试'
    
    def get_context(self): 
        return {
            'tops':[
                {'editor':'com-robot-receive',},
                {'editor':'com-rtc-recording'},
                {'editor':'com-rtc-put-task'},
                {'editor':'com-rtc-stop-robot'},
                #{'editor':'com-rtc-trigger'},
                #*rtc_send,
                #{'editor':'com-rtc-send'},
                #{'editor':'com-rtc-send'},
                #{'editor':'com-rtc-send'},
            ]
        }

@director_view('robot_receive_call')
def send_sss(src,dst,channel_name):
    robot_receive_call(src, dst, channel_name)

@director_view('robot_call_user')
def sss(src, dst_list, channel_name, taskid):
    robot_call_user(src, dst_list, channel_name, taskid)

@director_view('recording_test')
def recording_test(channel):
    recording(channel)
    #recording.delay(channel)

web_page_dc.update({
    'rtc-robot':RobotTestPage
})