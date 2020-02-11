from django.test import TestCase,Client
from .models import VoiceMsgList,CallTask
import json
from django.core.management import call_command
from unittest import mock
from django.utils import timezone
from functools import partial
# Create your tests here.
class TestSimpleWash(TestCase):
    
    def setUp(self):
        pass
    
    @mock.patch('part3.rabbit_instance.send_mp3')
    @mock.patch('django.utils.timezone.now')
    def test_call(self,mock_now,send_mp3):
        mocked_now = timezone.datetime.strptime('2020-01-01 10:10:10.664309','%Y-%m-%d %H:%M:%S.%f')
        mock_now.return_value  = mocked_now
        
        rabmq =[]
        def side_effect(usecase,rabmq,*args, **kwargs):
            rabmq.append(usecase)
            return print(usecase,str(args),str(kwargs))
        send_mp3.side_effect= partial(side_effect,'向rabbitmq发送MP3消息',rabmq)
        
        #def side_effect(*args, **kwargs):
            #return print('向rabbitmq发送MP3消息',str(args),str(kwargs))
        #send_mp3.side_effect= side_effect
        
        cl=Client(enforce_csrf_checks=True)

        #A 拨打
        rt = cl.post('/dapi/call/user',data={'src_uid':"1234",'dst_uid':'4321'})
        self.assertTrue( VoiceMsgList.objects.count() == 2)
        
        #B 拉取消息
        rt = cl.post('/dapi/call/msg',data={'uid':'4321'})
        channel = rt.json().get('data')[0].get('channel')
        
        #B 接收
        rt = cl.post('/dapi/call/recieve',data={'uid':'4321','channel':channel})
        self.assertTrue( VoiceMsgList.objects.get(uid='4321').status == 1 )
        
        #B 挂断
        rt = cl.post('/dapi/call/end',data={'uid':'4321','channel':channel})
        self.assertTrue( VoiceMsgList.objects.get(uid='4321').status == 2 )
        
        #A 挂断
        rt = cl.post('/dapi/call/end',data={'uid':'1234','channel':channel})
        self.assertTrue( VoiceMsgList.objects.get(uid='1234').status == 2 )
        
        # 上传拨打任务
        data = {'src_uid':'1234','dst_uid':['1235','1236'],'call_time':'2020-01-01 10:09:00',
                'tone_list':[
                    {"url":"/media/userfile/mytone1.mp3","before_second":10},                        
                    {"url":"/media/userfile/mytone2.mp3","before_second":20}
                ]}
        rt = cl.post('/dapi/calltask/update',data=json.dumps(data),content_type='application/json')
        self.assertTrue( CallTask.objects.filter(src_uid='1234').count() == 1 )
        
        # 获取拨打任务列表
        rt = cl.post('/dapi/calltask/list',data={'uid':'1234'})
        print('ss')
        
        call_command('calltask')
        self.assertTrue(len(rabmq) ==1)
        print('yy')