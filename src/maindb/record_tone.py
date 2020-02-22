import requests
from django.conf import settings
from urllib import parse
import base64

class ToneRecorder(object):
    
    def post(self,url,data):
        url = url%{
            'appid':settings.AGORA.get('rest_id')
        }
        ago_url = parse.urljoin('https://api.agora.io',url)
        heads = {
            'Authorization':base64.b64encode(settings.AGORA.get('rest_secret'))
        }
        rt = requests.post(ago_url,headers=heads,json=data)
        return rt.json()
    
    def acquire(self,channel):
        url ='/v1/apps/%(appid)s/cloud_recording/acquire'
        dc = {
            'cname':channel,
            'uid':231231,
            "clientRequest":{
                "resourceExpiredHour":  24
            }
        }
        rt = self.post(url,data=dc)
        print(rt)