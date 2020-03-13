from fastdog.maintain.filebeat.dfilebeat import DFileBeat,multi_tail_file,django_log_parsers,elastice_search,tail_file,nginx_log_parser
from functools import partial
from concurrent.futures import ThreadPoolExecutor,as_completed

p_django = DFileBeat(harvest= partial(multi_tail_file,
                                   [
                                       '/pypro/voiceplatform/log/process.log',
                                       '/pypro/voiceplatform/log/django.log'
                                   ]),
                  parsers =django_log_parsers,
                  outputs = [
                      partial(elastice_search,'liu.enjoyst.com:9200','elastic','he27375089','beat-voice')
                  ] )

p_nginx = DFileBeat(harvest= partial(tail_file,'/var/log/nginx/voiceplatform.log'),
                  parsers =nginx_log_parser,
                  outputs = [
                      partial(elastice_search,'liu.enjoyst.com:9200','elastic','he27375089','beat-voi-nginx')
                  ] )

executor =  ThreadPoolExecutor(max_workers = 2)
batch_items = [ p_django.run,p_nginx.run]
futures = [executor.submit(item) for item in batch_items]
for future in as_completed(futures):
    print(future.result() )