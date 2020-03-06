from helpers.director.shortcut import TablePage,ModelTable,page_dc,director
from .models import VoiceMsgList

class VoicemsgPage(TablePage):
    def get_label(self):
        return '语音消息'
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = VoiceMsgList
        exclude = []

director.update({
    'voicemsg':VoicemsgPage.tableCls
})

page_dc.update({
    'voicemsg':VoicemsgPage,
})