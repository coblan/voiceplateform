from helpers.director.shortcut import FieldsPage,Fields,page_dc,director,director_view
from helpers.director.kv import get_json,set_json
from django.conf import settings

class ConfigFormPage(FieldsPage):
    def get_label(self):
        return '前端配置管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/fields.html'
    
    class fieldsCls(Fields):
        def get_heads(self):
            return [
                {'name':'cfg_channel_heartbeat','label':'频道心跳间隔','editor':'com-field-number','fv_rule':'integer(+)','suffix':'秒'},
                {'name':'cfg_push_call_record','label':'电话记录推送地址','editor':'com-field-linetext'},
                {'name':'cfg_baidu_APPID','label':'百度APPID','editor':'com-field-linetext'},
                {'name':'cfg_baidu_API_KEY','label':'百度API_KEY','editor':'com-field-linetext'},
                {'name':'cfg_baidu_SECRECT_KEY','label':'百度SECRECT_KEY','editor':'com-field-linetext'},
            ]
        
        def dict_row(self):
            return {
                'cfg_channel_heartbeat':get_json('cfg_channel_heartbeat',30),
                'cfg_push_call_record':get_json('cfg_push_call_record',''),
                'cfg_baidu_APPID':get_json('cfg_baidu_APPID',''),
                'cfg_baidu_API_KEY':get_json('cfg_baidu_API_KEY',''),
                'cfg_baidu_SECRECT_KEY':get_json('cfg_baidu_SECRECT_KEY','')
            }
        
        def save_form(self):
            set_json('cfg_channel_heartbeat',self.kw.get('cfg_channel_heartbeat'))
            set_json('cfg_push_call_record',self.kw.get('cfg_push_call_record'))
            set_json('cfg_baidu_APPID',self.kw.get('cfg_baidu_APPID'))
            set_json('cfg_baidu_API_KEY',self.kw.get('cfg_baidu_API_KEY'))
            set_json('cfg_baidu_SECRECT_KEY',self.kw.get('cfg_baidu_SECRECT_KEY'))

@director_view('system/config')
def get_config():
    return {
        'channel_heartbeat':get_json('cfg_channel_heartbeat',30),
        'agora_appid':settings.AGORA.get('appID'),
        'baiduai_key':{
            'APPID':get_json('cfg_baidu_APPID',''),
            'API_KEY':get_json('cfg_baidu_API_KEY',''),
            'SECRECT_KEY':get_json('cfg_baidu_SECRECT_KEY',''),
        }
    }

director.update({
    'config':ConfigFormPage.fieldsCls
})

page_dc.update({
    'config':ConfigFormPage
})
        