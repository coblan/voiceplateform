from django.conf import settings
import pika
import json

#rabbitChanel=None
host = settings.RABBIT.get('host')
user = settings.RABBIT.get('user')
pswd = settings.RABBIT.get('pswd')
credentials = pika.PlainCredentials(user,pswd)
 
def send_msg(msg,uid):
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    jsonmsg = json.dumps({'msg':msg,'uid':uid},ensure_ascii=False)
    channel.basic_publish(exchange='usermsg',
                         routing_key= 'rtm-uid',
                         body=jsonmsg)

def send_mp3(rtc_channel,mp3_url):
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    jsonmsg = json.dumps({'channel':rtc_channel,'mp3_url':mp3_url},ensure_ascii=False)
    channel.basic_publish(exchange='user_rtc',
                         routing_key= 'user_rtc',
                         body=jsonmsg)