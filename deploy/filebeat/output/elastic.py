from elasticsearch import Elasticsearch,helpers

import logging
import socket
import datetime
import sys
import logging
general_log = logging.getLogger('general_log')

class ELKHander(logging.Handler):
    def __init__(self,host, user,pswd,index):
        self.index = index
        self.es = Elasticsearch(host,http_auth=(user,pswd ),timeout=100,max_retries=3)
        self.make_index()
        self.hostName = socket.gethostname()
        super().__init__()
        #print('elk-log1')
    
    def clean_hostname(self,msg):
        return {
            'msg':msg,
            'hostname':self.hostName
        }
    
    def make_index(self):
        _index_mappings = {
            "mappings": {
                "properties": { 
                  "@timestamp":    { "type": "date"  }, 
                  "level":     { "type": "text"  }, 
                  "host": {"type": "text"},
                  "message":      { "type": "text" }, 
                  "path":{"type": "text"}
                }
            }
          }
        if self.es.indices.exists(index= self.index ) is not True:
            res = self.es.indices.create(index = self.index, body=_index_mappings) 
    
    def send(self,lines):
        actions=[ ]
        for line in lines:
            actions.append({
                    "_index": self.index,
                    "_type": "_doc",
                    "_source": {
                        "level":line.get('level'),
                        "host":line.get('host',self.hostName),
                        "message":line.get('message'),
                        '@timestamp':line.get('@timestamp'),
                        "path":line.get('path')
                    }
            })
        helpers.bulk(self.es, actions)
    
    def emit(self, record): 
        msg =   record.getMessage()
        if record.levelname == 'ERROR':
            if record.exc_text:
                msg += '\n' + record.exc_text
            hostname= self.hostName
        else:
            dc = self.clean_hostname(msg)
            msg =  dc.get('msg')
            hostname = dc.get('hostname')
        dc = {
            '@timestamp': datetime.datetime.utcnow(),
            'level': record.levelname,
            'host': hostname , #self.hostName,
            'message': msg, #msg
        }
        try:
            res = self.es.index(self.index, doc_type='_doc', body = dc,request_timeout=100)
        except Exception as e:
            general_log.error('请求ELK出现了问题msg=%(msg)s,Exception= %(except)s' % {'msg':msg,'except':str(e)})



