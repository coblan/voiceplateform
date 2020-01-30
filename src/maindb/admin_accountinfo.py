from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,director_view,director_save_row
import json
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
    '''
    参数
    @uid  用户id,
    @device='',
    @apns_token=
    '''
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

#@director_view('account/reject-tone')
#def upload_reject_tone(uid,tone_url):
    #instacne = Accountinfo.objects.filter(uid = uid).first()
    #if instacne:
        #instacne.reject_tone = tone_url
        #instacne.save()
    #else:
        #raise UserWarning('用户不存在')
    
@director_view('account/reject-tone')
def upload_reject_tone(uid,tone_list):
    '''
    @uid:用户id
    @tone_list: [
        {'mp3':'/media/userfile/mytone1.mp3'},
        {'space_second':10000},
        {'mp3':'/media/userfile/mytone2.mp3'},
        {'space_second':20000},
        {'mp3':'/media/userfile/mytone2.mp3'},
    ]
    '''
    instacne = Accountinfo.objects.filter(uid = uid).first()
    if instacne:
        instacne.reject_tone = json.dumps(tone_list)
        instacne.save()
    else:
        raise UserWarning('用户不存在')

@director_view('account/get-reject-tone')
def get_reject_tone(uid):
    instacne = Accountinfo.objects.filter(uid = uid).first()
    if instacne :
        if instacne.reject_tone:
            return json.loads(instacne.reject_tone)
        else:
            return []
    else:
        raise UserWarning('用户不存在')

director.update({
    'accountinfo':AccountInfoPage.tableCls,
    'accountinfo.edit':AccountForm
})

page_dc.update({
    'accountinfo':AccountInfoPage
})