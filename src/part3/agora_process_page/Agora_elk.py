from helpers.director.shortcut import director_view
import json
import logging
rtc_log = logging.getLogger('rtc_log')

@director_view('rtc_front_log')
def rtc_front_log(msg,level='DEBUG'):
    #dc = {'msg':msg}
    send_msg = json.dumps(msg,ensure_ascii=False)
    if level == 'DEBUG':
        rtc_log.debug(send_msg)
    elif level == 'WARNING':
        rtc_log.warning(send_msg)
    else:
        rtc_log.info(send_msg)