from helpers.director.shortcut import ModelTable,TablePage,ModelFields,page_dc,director,RowFilter,director_view
from .models import FrontLog
class FrontLogPage(TablePage):
    def get_label(self):
        return '前端日志'
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = FrontLog
        exclude = []
        pop_edit_fields = ['id']
        
        def dict_head(self, head):
            width ={
                'key':130,
                'url':250,
            }
            if head['name'] in width:
                head['width']  = width.get(head['name'])
            return head
        
        class filters(RowFilter):
            range_fields = ['createtime']

class FrontLogForm(ModelFields):
    class Meta:
        model = FrontLog
        exclude =[]

@director_view('put-log')
def put_log(key,url):
    FrontLog.objects.create(key=key,url=url)

director.update({
    'frontlog':FrontLogPage.tableCls,
    'frontlog.edit':FrontLogForm,
})

page_dc.update({
    'frontlog':FrontLogPage
})

