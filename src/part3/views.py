from django.shortcuts import render

# Create your views here.
def voice_test(request):
    return render(request,'part3/voice_test.html',context={})

def rtm_page(request):
    return render(request,'part3/rtm_panel.html',context={})

def rtm_send(request):
    return render(request,'part3/rtm_send.html',context={})

def rtc_panel(request):
    return render(request,'part3/rtc_panel.html',context={})

def rtc_send(request):
    return render(request,'part3/rtc_send.html',context={})