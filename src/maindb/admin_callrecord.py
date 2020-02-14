from helpers.director.shortcut import TablePage,ModelTable,director,page_dc,director_view
from .models import CallRecord,CallEvent
from django.utils import timezone
from helpers.func.sim_signal import sim_signal
from django.db.models import OuterRef, Subquery,F

class CallRecordPage(TablePage):
    def get_label(self):
        return '通话记录'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = CallRecord
        exclude =[]

#@director_view('call/enter')
#def call_enter(uid,channel):
    #sim_signal.send('call.enter',uid=uid,channel=channel)

@director_view('call/heartbeat')
def refresh_call_record(channel):
    CallRecord.objects.filter(channel=channel).update(refreshtime=timezone.now())

@director_view('call/event')
def event_call_record(uid,channel,code,desp=''):
    #try:
        #record = CallRecord.objects.get(channel=channel)
    #except CallRecord.DoesNotExist:
        #record = None
    
    obj = CallEvent.objects.create(uid=uid,channel=channel,code=code,desp=desp)
    
    latest = CallRecord.objects.filter(channel=OuterRef('channel'))
    #CallEvent.objects.filter(pk = obj.pk).annotate(record_me = Subquery(latest.values('pk')[:1])).update(record_id=F('record_me'))
    CallEvent.objects.filter(pk = obj.pk).update(record_id= Subquery(latest.values('pk')[:1]) )



director.update({
    'callrecord':CallRecordPage.tableCls
})

page_dc.update({
    'callrecord':CallRecordPage
})