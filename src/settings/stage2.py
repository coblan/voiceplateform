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

ALLOWED_HOSTS=['liu.enjoyst.com','localhost']

AGORA={
    'appID':'303156d224e44881a00af9cabc9e10d8',
    'appCertificate':'0ca642eb8e3a4c868822af7e4d0dfee9'
}

RABBIT={
    'host':'localhost',
    'user':'guest',
    'pswd':'guest',
}
WEBSOCKET = {
    'url':'wss://liu.enjoyst.com:10831/ws',
    'user':'voice',
    'pswd':'voice',
}

ELK={
    'host':'http://localhost:9200',
    'user':'elastic',
    'pswd':'he27375089',
    'voice_rtm_msg':'voice_rtm_msg',
    'voiceplatform':'voiceplatform'
}

APPLE={
    'push_crt':'dev_123456.pem'
}

from . log import *

APP_HOST= 'http://uys8je.natappfree.cc' #'http://kukpyk.natappfree.cc'
REJECT_WATI = 30  # 废弃

RECORD={
    'lowUdpPort':14000,
    'highUdpPort':15000,
    'recorder_local':'/root/agoracore/Agora_Recording_SDK_for_Linux_FULL/samples/cpp/recorder_local',
    'recording_bin':'/root/agoracore/Agora_Recording_SDK_for_Linux_FULL/bin',
    'tone_dir':'/userfile/recording',
    'idle':'2',
}