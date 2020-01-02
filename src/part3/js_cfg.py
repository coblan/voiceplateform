from helpers.director.base_data import  js_lib_list
from django.utils.translation import ugettext as _
from helpers.maintenance.update_static_timestamp import js_stamp_dc


def get_lib(request): 
    dc = {
        'myagora': '/static/js/myagora.pack.js?t=%s&v=1'%js_stamp_dc.get('myagora_pack_js'), 
    }
    return dc

js_lib_list.append(get_lib)