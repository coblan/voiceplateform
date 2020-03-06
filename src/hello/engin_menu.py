
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine, page, fa, can_list, can_touch
from django.contrib.auth.models import User, Group
from helpers.func.collection.container import evalue_container
from helpers.maintenance.update_static_timestamp import js_stamp
from django.utils.translation import ugettext as _
from django.conf import settings
from helpers.director.access.permit import has_permit
from helpers.pcweb.shotcut import web_page_dc

class PcAdminMenu(BaseEngine):
    url_name = 'BackEnd'
    title = 'BackEnd'
    brand = 'BackEnd'
    mini_brand = 'BackEnd'
    need_staff=True
    need_login=True
    access_from_internet=True
    @property
    def menu(self):
        crt_user = self.request.user
        menu = [
            {'label': '通话管理', 'visible': True,'submenu':[
                {'label': '通话记录', 'url': page('callrecord'), 'visible': True},
                {'label': '定时任务', 'url': page('calltask'), 'visible': True},
                #{'label':'用户语音消息','url':page('voicemsg'),},
            ]},
           
            {'label': '配置管理', 'url': page('config'), 'visible': True},
            {'label': '模拟api', 'url': page('mockapi'), 'visible': True},
            
        ]

        return menu
    

PcAdminMenu.add_pages(page_dc)


class AgoraProcessEngin(BaseEngine):
    url_name = 'SoftJing'
    title = 'SoftJing'
    brand = 'SoftJing'
    mini_brand = 'SoftJing'
    need_staff=False
    need_login=False
    access_from_internet=True
    @property
    def menu(self):
        crt_user = self.request.user
        menu = [
        
            #{'label': '首页', 'url': page('home'), 'visible': True},
            #{'label': '文章','url':page('articlelist'), 'visible': True},
            #{'label': '示例','url':page('example'), 'visible': True},
            #{'label':'后台管理','url':'/pc/admin_article','visible':True},
        ]

        return menu
    
    def custome_ctx(self, ctx):
        if 'extra_js' not in ctx:
            ctx['extra_js'] = []
        if 'myagora' not in ctx['extra_js']:
            #ctx['extra_js'].append('https://cdn.jsdelivr.net/npm/@elastic/elasticsearch@7.5.0/index.min.js')
            ctx['extra_js'].append('myagora')
            
        return ctx
    
        #ctx.update({
            #'navibar':{
                #'editor':'com-xiu-menu',
            #},
            #'footer':{
                #'editor':'com-ft-copyright','copyright':'@copyright 2019 jingjia Infomaion Technology Co'
            #},
            #'customize_meta':'''<meta name="keywords" content="互联网 软件 管理后台 公众号" />
#<meta name="description" content="竞嘉信息技术有限公司">
#<meta name="author" content="竞嘉信息技术有限公司">'''
        #})
        #return ctx

AgoraProcessEngin.add_pages(web_page_dc)


