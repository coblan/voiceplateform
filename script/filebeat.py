import os
os.environ['geo_db'] = '/userfile/GeoLite2-City.mmdb'

from fastdog.maintain.filebeat.dfilebeat import DFileBeat,multi_tail_file,django_process_parsers,elastice_output,nginx_log_parser,\
     elasticesearch_process
from fastdog.maintain.fast_log import set_log
from fastdog.maintain.filebeat.output.elastic_process import ELKProcess
from fastdog.maintain.filebeat.output.elastic_nginx import ELKNginx

from functools import partial
from concurrent.futures import ThreadPoolExecutor,as_completed
base_dir = os.path.dirname(  os.path.dirname( os.path.abspath(__file__) )  )
log_path = os.path.join( base_dir,'log/filebeat.log')
set_log(log_path)

p_django = DFileBeat(harvest= partial(multi_tail_file,
                                   [
                                       '/pypro/voiceplatform/log/process.log',
                                       '/pypro/voiceplatform/log/django.log'
                                   ]),
                  parsers =django_process_parsers,
                  outputs = [
                      partial(elastice_output,'liu.enjoyst.com:9200','elastic','he27375089','voice-django',ELKProcess)
                  ] )

p_nginx = DFileBeat(harvest= partial(multi_tail_file,['/var/log/nginx/voiceplatform.log']),
                  parsers =nginx_log_parser,
                  outputs = [
                      partial(elastice_output,'liu.enjoyst.com:9200','elastic','he27375089','voice-nginx',ELKNginx)
                  ] )

executor =  ThreadPoolExecutor(max_workers = 2)
batch_items = [ p_django.run,p_nginx.run]
futures = [executor.submit(item) for item in batch_items]
for future in as_completed(futures):
    print(future.result() )