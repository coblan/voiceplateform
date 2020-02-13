from helpers.director.shortcut import TablePage,ModelTable,director,page_dc,director_view
from .models import CallRecord
from django.utils import timezone
from helpers.func.sim_signal import sim_signal

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
    

director.update({
    'callrecord':CallRecordPage.tableCls
})

page_dc.update({
    'callrecord':CallRecordPage
})