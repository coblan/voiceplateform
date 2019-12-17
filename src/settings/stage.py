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

AGORA={
    'appID':'303156d224e44881a00af9cabc9e10d8',
    'appCertificate':'0ca642eb8e3a4c868822af7e4d0dfee9'
}