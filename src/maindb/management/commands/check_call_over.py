
from django.core.management.base import BaseCommand
from django.conf import settings
from helpers.director.base_data import director
from django.utils import timezone
from helpers.func.random_str import get_str
from part3.apple.apns import VoiceCallPush
from maindb.models import CallRecord
from part3. rabbit_instance import send_msg,send_mp3
import json
from helpers.func.sim_signal import sim_signal

import logging
general_log = logging.getLogger('general_log')

class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):
        now = timezone.now()
        valid_time = now - timezone.timedelta(seconds = 30)
        for record in  CallRecord.objects.filter(refreshtime__lte= valid_time,starttime__isnull=False,endtime__isnull=True,):
            record.endtime = now
            record.save()
            sim_signal.send('call.end',record)
        
        general_log.debug('定时拨打任务结束')
    

    
