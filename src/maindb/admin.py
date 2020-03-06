from django.contrib import admin

# Register your models here.
from . import signal
from . import admin_accountinfo
from . import admin_calltask
from . import admin_callrecord
from . import admin_config
from . import admin_mockapi
from . import admin_voicemsg
from . import admin_frontlog

from .pc_page import panel

from helpers.director.base_data import inspect_dict

from helpers.pcweb.shotcut import web_page_dc

inspect_dict['web_page_dc'] = web_page_dc
