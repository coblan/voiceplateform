from helpers.director.shortcut import TablePage,ModelTable,director,page_dc,director_view,RowFilter
from .models import CallRecord,CallEvent
from django.utils import timezone
from helpers.func.sim_signal import sim_signal
from django.db.models import OuterRef, Subquery,F,Count


class CallRecordPage(TablePage):
    def get_label(self):
        return '通话记录'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = CallRecord
        exclude =[]
        
        def getExtraHead(self):
            return [
                {'name':'event_count','label':'事件数量','editor':'com-table-span'}
            ]
        
        def inn_filter(self, query):
            return query.annotate(event_count = Count('callevent') )
        
        def dict_row(self, inst):
            return {
                'event_count':inst.event_count
            }
        
        def dict_head(self, head):
            if head['name'] =='event_count':
                head['editor']='com-table-click'
                head['action']='scope.head.table_ctx.search_args._par=scope.row.pk;cfg.pop_vue_com("com-table-panel",scope.head.table_ctx)'
                head['table_ctx']=CallEventTab().get_head_context()
            return head
        
        class filters(RowFilter):
            range_fields=['starttime']

class CallEventTab(ModelTable):
    model = CallEvent
    exclude =['record']
    
    def inn_filter(self, query):
        return query.filter(record_id = self.search_args.get('_par'))

@director_view('call/heartbeat')
def refresh_call_record(uid,channel):
    "客户端心跳，标识channel有人"
    CallRecord.objects.filter(channel=channel).update(refreshtime=timezone.now())

@director_view('call/event')
def event_call_record(uid,channel,code,desp=''):
    #try:
        #record = CallRecord.objects.get(channel=channel)
    #except CallRecord.DoesNotExist:
        #record = None
    """
    客户端上报channel事件
    
    code:
    1. 用户进入
    2. 用户退出
    
    """
    if int(code) == 1 :
        sim_signal.send('call.enter',uid=uid,channel=channel)
    if int(code) ==2:
        sim_signal.send('call.quit',uid=uid,channel=channel)
        
    obj = CallEvent.objects.create(uid=uid,channel=channel,code=code,desp=desp)
    latest = CallRecord.objects.filter(channel=OuterRef('channel'))
    #CallEvent.objects.filter(pk = obj.pk).annotate(record_me = Subquery(latest.values('pk')[:1])).update(record_id=F('record_me'))
    CallEvent.objects.filter(pk = obj.pk).update(record_id= Subquery(latest.values('pk')[:1]) )



director.update({
    'callrecord':CallRecordPage.tableCls,
    'callevent-tab':CallEventTab
})

page_dc.update({
    'callrecord':CallRecordPage
})