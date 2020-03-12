from dfilebeat import DFileBeat,multi_tail_file,django_log_parsers


pp = DFileBeat(harvest= partial(multi_tail_file,
                                   [
                                       '/pypro/voiceplatform/log/process.log',
                                   ]),
                  parsers =django_log_parsers,
                  outputs = [
                      partial(elastice_search,'liu.enjoyst.com:9200','elastic','he27375089','beat-voice')
                  ] )
pp.run()