from django.conf import settings
import pika
import json

#rabbitChanel=None
host = settings.RABBIT.get('host')
user = settings.RABBIT.get('user')
pswd = settings.RABBIT.get('pswd')
credentials = pika.PlainCredentials(user,pswd)

def init():
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='usermsg', exchange_type='topic')
    channel.exchange_declare(exchange='user_rtc', exchange_type='topic')
    channel.exchange_declare(exchange='stop_channel', exchange_type='topic')

init()

def send_msg(msg,uid):
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    jsonmsg = json.dumps({'msg':msg,'uid':uid},ensure_ascii=False)
    channel.basic_publish(exchange='usermsg',
                         routing_key= 'rtm-uid',
                         body=jsonmsg)

def send_mp3(rtc_channel,tone_list,src_uid=None):
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    jsonmsg = json.dumps({'channel':rtc_channel,'tone_list':tone_list,'src_uid':src_uid},ensure_ascii=False)
    channel.basic_publish(exchange='user_rtc',
                         routing_key= 'user_rtc',
                         body=jsonmsg)

def notify_quit_robot(channel_name):
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    #jsonmsg = json.dumps({'channel':rtc_channel,'mp3_url':mp3_url},ensure_ascii=False)
    channel.basic_publish(exchange='stop_channel',
                         routing_key= channel_name,
                         body='stop-channel')