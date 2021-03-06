"""voiceplateform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
#from django.contrib import admin
#from hello.engin_menu import PcWebMenu,PcAdminMenu
from django.conf.urls.static import static
from helpers.director.views import director_view
from django.conf import settings
from django.views.generic import RedirectView 
from helpers.authuser.engin_view import AuthEngine
from hello.views import relay
from part3 import views as part3_views
from hello.engin_menu import AgoraProcessEngin,PcAdminMenu

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url('voice_test',part3_views.voice_test),
    url('^rtm/?$',part3_views.rtm_page),
    url('^rtm_send/?$',part3_views.rtm_send),
    url('^rtc/?$',part3_views.rtc_panel),
    url('^rtc_send/?$',part3_views.rtc_send),
    
    url(r'^ago/([\w\.-]+)/?$',AgoraProcessEngin.as_view(),name=AgoraProcessEngin.url_name),
    
    url(r'^relay/?$',relay),
    url(r'^accounts/([\w\.]+)/?$',AuthEngine.as_view(),name=AuthEngine.url_name),
    url(r'^pc/([\w\.-]+)/?$',PcAdminMenu.as_view(),name=PcAdminMenu.url_name),
    url(r'^d/',include('helpers.director.urls'),name='director'),
    url(r'^dapi/(?P<director_name>[\w\/\.-]+)?/?$',director_view),
    url(r'^p$',RedirectView.as_view(url='/ago/p')) ,
    url(r'^$',RedirectView.as_view(url='/pc/callrecord')) ,
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)