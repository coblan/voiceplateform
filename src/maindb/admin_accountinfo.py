from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,director_view,director_save_row

from .models import Accountinfo

class AccountInfoPage(TablePage):
    def get_label(self):
        return '用户信息'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = Accountinfo
        exclude =[]

class AccountForm(ModelFields):
    nolimit = True
    class Meta:
        model = Accountinfo
        exclude =[]

@director_view('account/update')
def update_account_info(**kws):
    'uid,device='',apns_token='''
    instacne = Accountinfo.objects.filter(uid = kws.get('uid')).first()
    if instacne:
        pk = instacne.pk
    else:
        pk = None
    kws.update({
        '_director_name':'accountinfo.edit',
        'pk':pk
    })
    return director_save_row(kws)

director.update({
    'accountinfo':AccountInfoPage.tableCls,
    'accountinfo.edit':AccountForm
})

page_dc.update({
    'accountinfo':AccountInfoPage
})