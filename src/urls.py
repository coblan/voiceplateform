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

from part3 import views as part3_views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url('voice_test',part3_views.voice_test),
    url(r'^accounts/([\w\.]+)/?$',AuthEngine.as_view(),name=AuthEngine.url_name),
    #url(r'^pc/([\w\.]+)/?$',PcAdminMenu.as_view(),name=PcAdminMenu.url_name),
    url(r'^d/',include('helpers.director.urls'),name='director'),
    url(r'^dapi/(?P<director_name>[\w\/\.-]+)?/?$',director_view),
    url(r'^$',RedirectView.as_view(url='/web/home')) ,
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)