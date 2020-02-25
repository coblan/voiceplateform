from django.test import TestCase,Client
from .models import VoiceMsgList,CallTask,CallRecord,CallEvent
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
        self.assertTrue( CallRecord.objects.count() == 1)
        
        # A 进入频道
        rt = cl.post('/dapi/call/event',data={'uid':'1234','channel':rt.json().get('data').get('channel'),'code':1})
        self.assertTrue( CallRecord.objects.first().count == 1)
        self.assertEqual(CallEvent.objects.count(),1)
        
        #B 拉取消息
        rt = cl.post('/dapi/call/msg',data={'uid':'4321'})
        channel = rt.json().get('data')[0].get('channel')
        self.assertTrue(CallRecord.objects.first().channel == channel)
        
        #B 接收
        rt = cl.post('/dapi/call/event',data={'uid':'4321','channel':channel,'code':1})
        self.assertTrue( VoiceMsgList.objects.get(uid='4321').status == 1 )
        self.assertTrue(CallRecord.objects.first().count == 2)
        
        #B 挂断
        rt = cl.post('/dapi/call/event',data={'uid':'4321','channel':channel,'code':2})
        self.assertTrue( VoiceMsgList.objects.get(uid='4321').status == 2 )
        self.assertTrue(CallRecord.objects.first().count == 1)
        
        #A 挂断
        rt = cl.post('/dapi/call/event',data={'uid':'1234','channel':channel,'code':2})
        self.assertTrue( VoiceMsgList.objects.get(uid='1234').status == 2 )
        self.assertTrue(CallRecord.objects.first().count == 0)
        self.assertTrue(CallRecord.objects.first().endtime)
        self.assertEqual(CallEvent.objects.count(),4)
        
        # 上传拨打任务
        data = {'src_uid':'1234',
                'dst_uid':['1235','1236'],
                'call_time':'2020-01-01 10:09:00',
                'taskid':123}
        rt = cl.post('/dapi/calltask/update',data=json.dumps(data),content_type='application/json')
        self.assertTrue( CallTask.objects.filter(src_uid='1234').count() == 1 )
        
        # 获取拨打任务列表 [现在可能去app后台获取了，这个接口应该无用了]
        rt = cl.post('/dapi/calltask/list',data={'uid':'1234'})
        
        call_command('calltask')
        self.assertTrue(len(rabmq) ==1)
        
        call_record = CallRecord.objects.create(src_uid='11',dst_uid=['23','44'],channel='ch_12345',starttime='2020-01-01 10:06:00',refreshtime='2020-01-01 10:07:00')
        call_command('check_call_over')
        
        rt = cl.post('/dapi/call/event',data={'uid':'1234','channel':"ch_12345",'code':123,"desp":'ppp'})
        self.assertEqual(CallEvent.objects.count(),6)
        print('yy')
        