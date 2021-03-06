from helpers.director.shortcut import ModelTable,TablePage,ModelFields,page_dc,director,director_view,director_save_row
from .models import CallTask

class CallTaskPage(TablePage):
    def get_label(self):
        return '拨打任务'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = CallTask
        exclude =[]
        pop_edit_fields=['id']
        
        def dict_head(self, head):
            width={
                'src_uid':150,
                'dst_uid':200,
            }
            if head['name'] in width:
                head['width'] = width.get(head['name'])
            return head
        
class CallTaskForm(ModelFields):
    nolimit = True
    class Meta:
        model = CallTask
        exclude = []

class UserCallTask(ModelTable):
    model = CallTask
    exclude = []
    nolimit = True
    simple_dict=True
    def inn_filter(self, query):
        return query.filter(src_uid = self.kw.get('uid'))

@director_view('calltask/update')
def update_calltask(**row):
    """
    普通用户上传或者更改定时任务。
    
    src_uid:
    dst_uid:
    call_time:
    """
    taskid = row.get('taskid')
    inst,_ = CallTask.objects.get_or_create(taskid = taskid)
    inst.src_uid = row.get('src_uid')
    inst.dst_uid= row.get('dst_uid')
    inst.call_time=row.get('call_time')
    inst.save()
    #row['_director_name'] = 'calltask.edit'
    #return director_save_row(row)

@director_view('calltask/delete')
def delete_call_task(taskid):
    CallTask.objects.filter(taskid = taskid).delete()

#@director_view('call/test')
#def testmy(**kws):
# "测试了下推送通话记录到外部系统"
    #print(kws)

director.update({
    'calltask':CallTaskPage.tableCls,
    'calltask.edit':CallTaskForm,
    'calltask/list':UserCallTask
})

page_dc.update({
    'calltask':CallTaskPage,
})