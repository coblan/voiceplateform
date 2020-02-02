from django.test import TestCase,Client
from .models import VoiceMsgList,CallTask
import json

# Create your tests here.
class TestSimpleWash(TestCase):
    
    def setUp(self):
        pass
    
    def test_call(self):
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
        data = {'src_uid':'1234','dst_uid':['1235','1236'],'call_time':'2020-02-02 20:20:00',}
        rt = cl.post('/dapi/calltask/update',data=json.dumps(data),content_type='application/json')
        self.assertTrue( CallTask.objects.filter(src_uid='1234').count() == 1 )
        
        # 获取拨打任务列表
        rt = cl.post('/dapi/calltask/list',data={'uid':'1234'})
        print('ss')
        