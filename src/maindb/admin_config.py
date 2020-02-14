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
                {'name':'cfg_channel_heartbeat','label':'频道心跳间隔','editor':'com-field-number','fv_rule':'integer(+)','suffix':'秒'}
            ]
        
        def dict_row(self):
            return {
                'cfg_channel_heartbeat':get_json('cfg_channel_heartbeat',30)
            }
        
        def save_form(self):
            set_json('cfg_channel_heartbeat',self.kw.get('cfg_channel_heartbeat'))

@director_view('system/config')
def get_config():
    return {
        'channel_heartbeat':get_json('cfg_channel_heartbeat',30),
        'agora_appid':settings.AGORA.get('appID'),
    }

director.update({
    'config':ConfigFormPage.fieldsCls
})

page_dc.update({
    'config':ConfigFormPage
})
        