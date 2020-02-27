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
    #channel.exchange_declare(exchange='stop_channel', exchange_type='topic')
    channel.exchange_declare(exchange='rtc-robot.stop', exchange_type='topic')
    
    
    channel.exchange_declare(exchange='rtc-robot', exchange_type='topic')
    
    channel.exchange_declare(exchange='user_rtc', exchange_type='topic')
    
    channel.queue_declare('rtc-robot.call',durable=True)
    channel.queue_bind( exchange='rtc-robot', queue='rtc-robot.call', routing_key='call')
    
    channel.queue_declare('rtc-robot.receive',durable=True)
    channel.queue_bind( exchange='rtc-robot', queue='rtc-robot.receive', routing_key='receive')

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

def robot_receive_call(src,dst,channel_name):
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    jsonmsg = json.dumps({'from':src,'to':dst,'channel':channel_name,},ensure_ascii=False)
    channel.basic_publish(exchange='rtc-robot',
                         routing_key= 'receive',
                         body=jsonmsg)


def robot_call_user(src,dst_list,channel_name,taskid):
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    jsonmsg = json.dumps({'from':src,'to':dst_list,'channel':channel_name,'taskid':taskid},ensure_ascii=False)
    channel.basic_publish(exchange='rtc-robot',
                         routing_key= 'call',
                         body=jsonmsg)


def notify_quit_robot(channel_name,uid):
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    jsonmsg = json.dumps({'channel':channel_name,'uid':uid},ensure_ascii=False)
    channel.basic_publish(exchange='rtc-robot.stop',
                         routing_key= channel_name,
                         body=jsonmsg)