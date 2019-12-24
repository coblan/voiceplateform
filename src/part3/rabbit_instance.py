from django.conf import settings
import pika
import json

#rabbitChanel=None

def send_msg(msg,uid):
    host = settings.RABBIT.get('host')
    user = settings.RABBIT.get('user')
    pswd = settings.RABBIT.get('pswd')
    credentials = pika.PlainCredentials(user,pswd)
    connection =pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
    channel = connection.channel()
    jsonmsg = json.dumps({'msg':msg,'uid':uid},ensure_ascii=False)
    channel.basic_publish(exchange='usermsg',
                         routing_key= 'rtm-uid',
                         body=jsonmsg)