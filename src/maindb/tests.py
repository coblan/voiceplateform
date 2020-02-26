from django.test import TestCase,Client
from .models import VoiceMsgList,CallTask,CallRecord,CallEvent
import json
from django.core.management import call_command
from unittest import mock
from django.utils import timezone
from functools import partial
from maindb.tasks import channel_reject_monitor,check_is_receive
# Create your tests here.

class Myobjet(object):
    pass

class TestSimpleWash(TestCase):
    
    def setUp(self):
        self.mock_all()
        
    
    def mock_all(self):
        self.now_pather = mock.patch('django.utils.timezone.now')
        self.channel_monitor_patcher = mock.patch('maindb.tasks.channel_reject_monitor.delay')
        self.check_receive_patcher = mock.patch('maindb.tasks.check_is_receive.apply_async')
        self.request_post_patcher = mock.patch('requests.post')
        
        self.mock_now = self.now_pather.start()
        self.mock_now.return_value  = timezone.datetime.strptime('2020-01-01 10:10:10.664309','%Y-%m-%d %H:%M:%S.%f')
        
        monitor = self.channel_monitor_patcher.start()
        monitor.side_effect = channel_reject_monitor
        
        def function_side_effect(usecase,*args, **kwargs):
            return print(usecase,args,json.dumps( kwargs) )
        check_receive = self.check_receive_patcher.start()
        check_receive.side_effect = partial(function_side_effect,'< 准备延迟检测是否有人接听 >')
        
        def request_side_effect(url,*args, **kwargs):
            if url == 'http://kukpyk.natappfree.cc/extphone_new/ext/setting/call':
                print('< 请求app后端获取用户等待时间 >',str(args),str(kwargs))
                obj = Myobjet()
                obj.text='{"text":"测试app服务器返回内容"}'
                obj.status_code = 200
                obj.json = lambda :{'data':{'data':{"waitTime":20}} }
                return obj
        
        request_post = self.request_post_patcher.start()
        request_post.side_effect = request_side_effect
        
        pika_connection = mock.patch('pika.BlockingConnection').start()
        connection = Myobjet()
        channel = Myobjet()
        def mq_side_effect(*args, **kwargs):
            kwargs['body'] = json.loads(kwargs['body'])
            print(kwargs)
        channel.basic_publish = mq_side_effect
        connection.channel = lambda:channel
        pika_connection.return_value = connection
        
    
    def tearDown(self):
        self.now_pather.stop()
        self.channel_monitor_patcher.stop()
        self.check_receive_patcher.stop()
        self.request_post_patcher.stop()
        
    def test_call(self):

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
        #self.assertTrue(len(rabmq) ==1)
        
        call_record = CallRecord.objects.create(src_uid='11',dst_uid=['23','44'],channel='ch_12345',starttime='2020-01-01 10:06:00',refreshtime='2020-01-01 10:07:00')
        call_command('check_call_over')
        
        rt = cl.post('/dapi/call/event',data={'uid':'1234','channel':"ch_12345",'code':123,"desp":'ppp'})
        self.assertEqual(CallEvent.objects.count(),6)
        print('='*30)
    
    def test_check(self):
        cl=Client(enforce_csrf_checks=True)
        
        #A 拨打
        rt = cl.post('/dapi/call/user',data={'src_uid':"1234",'dst_uid':'4321'})
        self.mock_now.return_value = timezone.datetime.strptime('2020-01-01 10:10:40.664309','%Y-%m-%d %H:%M:%S.%f')
        channel = rt.json().get('data').get('channel')
        check_is_receive(channel)
        print('='*30)
    
    def test_event(self):
        cl=Client(enforce_csrf_checks=True)
        
        rt = cl.post('/dapi/call/user',data={'src_uid':"1234",'dst_uid':'4321'})
        data = {
            "uid":"12345",
            "channel":rt.json().get('data').get('channel'),
            "code":1, 
            "desp":"接通",
        }
        rt = cl.post('/dapi/call/event',data=data)
        print('='*30)
        
    
        