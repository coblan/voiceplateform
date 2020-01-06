import socket, ssl, json, struct
import binascii
import sys
import os

def Payload(alert='', badge=1, data={}):
    payload = {
       'aps': {
           'alert':alert,
           'sound':'k1DiveAlarm.caf',
           'badge':badge,
        },
       'acme': data,
    }
    #{
    #"aps": {
        #"content-available": 1,
        #"alert": {
            #"title": "hello",
            #"body": "Your message1 here."
        #},
        #"badge": 9,
        #"sound": "default",
        #"userInfo": {
            #"key1": "value1",
            #"key2": "value2"
        #}
    #}
    #}
    
    
    return payload

def APN(token, payload, theCertfile):
    #theHost = ( 'gateway.push.apple.com', 2195 )
    theHost = ( 'gateway.sandbox.push.apple.com', 2195 )
    data = json.dumps( payload )

    # Clear out spaces in the device token and convert to hex
    deviceToken = token.replace(' ','')
    #byteToken = binascii.unhexlify(token)
    byteToken = binascii.unhexlify(deviceToken)
    
    theFormat = b'!BH32sH%ds' % len(data)
    theNotification = struct.pack( theFormat, 0, 32, byteToken, len(data), data.encode('utf-8') )

    # Create our connection using the certfile saved locally
    ssl_sock = ssl.wrap_socket(
            socket.socket( socket.AF_INET, socket.SOCK_STREAM ),
            certfile = theCertfile
        )
    ssl_sock.connect( theHost )

    # Write out our data
    ssl_sock.write( theNotification )

    # Close the connection -- apple would prefer that we keep
    # a connection open and push data as needed.
    ssl_sock.close()

    return True



pp = os.path.dirname(__file__)
pem_path = os.path.join(pp,'apn.pem')
def push(msg):
    #推送需要用到的证书
    
    pem = pem_path
    token = msg['udid']
    data = msg['data']

    payload = Payload(msg['content'], msg['count'], data)
    return APN(token, payload, pem)

if __name__ == '__main__':
    msg = {
        'data': {'type':'feed', 'id': 123},
        'count': 8,
        'udid': 'f435d683eb9d7e5680938c363ea6e38eba36a553e9b23ddd57f9xxxxxxxxxxxx',
        'content': 'ios推送测试'
    }
    print ( push(msg) )