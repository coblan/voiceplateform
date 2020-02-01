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
    src_uid:
    dst_uid:
    call_time:
    """
    row['_director_name'] = 'calltask.edit'
    return director_save_row(row)


director.update({
    'calltask':CallTaskPage,
    'calltask.edit':CallTaskForm,
    'calltask/list':UserCallTask
})