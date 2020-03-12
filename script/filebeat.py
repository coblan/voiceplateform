from fastdog.maintain.filebeat.dfilebeat import DFileBeat,multi_tail_file,django_log_parsers,elastice_search
from functools import partial

pp = DFileBeat(harvest= partial(multi_tail_file,
                                   [
                                       '/pypro/voiceplatform/log/process.log',
                                       '/pypro/voiceplatform/log/django.log'
                                   ]),
                  parsers =django_log_parsers,
                  outputs = [
                      partial(elastice_search,'liu.enjoyst.com:9200','elastic','he27375089','beat-voice')
                  ] )
pp.run()