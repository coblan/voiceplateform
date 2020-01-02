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

ALLOWED_HOSTS=['voice.enjoyst.com','localhost']

AGORA={
    'appID':'303156d224e44881a00af9cabc9e10d8',
    'appCertificate':'0ca642eb8e3a4c868822af7e4d0dfee9'
}

RABBIT={
    'host':'localhost',
    'user':'guest',
    'pswd':'guest',
}

ELK={
    'host':'http://localhost:9200',
    'user':'elastic',
    'pswd':'he27375089',
}

import os
LOG_PATH= os.path.join( os.path.dirname(BASE_DIR),'log')

LOGGING = {
    'version': 1, # 标示配置模板版本，int 类型，目前只接收 `1`这个值。
    'disable_existing_loggers': False, 
    'formatters': {
        'standard': {
             'format': '%(levelname)s %(asctime)s %(message)s',
        },
    },
    'filters': {
        # 这里是定义过滤器，需要注意的是，由于 'filters' 是 logging.config.dictConfig 方法要求在配置字典中必须给订的 key ,所以即使不使用过滤器也需要明确给出一个空的结构。
    },
    'handlers': {
         'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter':'standard',
        },
        'rtc_log':{
            'level': 'DEBUG',
            'class': 'hello.elk.RTCLOG',         
            },    
        'console': {
            'level':'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
            },  
        'djangoout_warning':{
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*5,
            'backupCount':3,
            'formatter':'standard',
            'filename': os.path.join(LOG_PATH,'django.log'),            
            },        
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'djangoout_warning', 'mail_admins'],
            'level': 'INFO',
            },
         'rtc_log': {
            'handlers': ['console', 'rtc_log', ],
            'level': 'DEBUG',
            'propagate': True,            
            },
        'general_log': {
            'handlers': ['console', 'djangoout_warning',  ],
            'level': 'DEBUG',
            'propagate': True,            
            },
 
    }
}
