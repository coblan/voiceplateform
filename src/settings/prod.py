from .base import *

import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
     'default': {
        'NAME': 'voiceplatform',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root553',
        'HOST': '127.0.0.1', 
        'PORT': '3306', 
        'OPTIONS': {'charset':'utf8mb4'},

      },
} 

ALLOWED_HOSTS=['www.fenji.xyz','localhost']

DEBUG =False

AGORA={
    'appID':'1f74816f860048d3a92cc48784fcc2d4',
    'appCertificate':'0d615a1312e1436b8c2f4e70e648b7cb'
}

RABBIT={
    'host':'localhost',
    'user':'guest',
    'pswd':'guest',
}
#WEBSOCKET = {
    #'url':'wss://liu.enjoyst.com:10831/ws',
    #'user':'voice',
    #'pswd':'voice',
#}

#ELK={
    #'host':'http://localhost:9200',
    #'user':'elastic',
    #'pswd':'he27375089',
    #'voice_rtm_msg':'voice_rtm_msg',
    #'voiceplatform':'voiceplatform'
#}

APPLE={
    'push_crt':'dev_123456.pem'
}

from . log import *

APP_HOST= 'http://hxqtest.natapp1.cc'  # 'http://hpfi9z.natappfree.cc' #'http://kukpyk.natappfree.cc'


SELF_DOMAIN = 'https://www.fenji.xyz'
import urllib

RECORD={
    'lowUdpPort':14000,
    'highUdpPort':15000,
    'recorder_local':'/userfile/agora_record_sdk/samples/cpp/recorder_local',
    'recording_bin':'/userfile/agora_record_sdk/bin',
    'tone_dir': os.path.join(MEDIA_ROOT,'recording'),
    'tone_url':urllib.parse.urljoin(SELF_DOMAIN, '/media/recording/'),
    'idle':3,
}