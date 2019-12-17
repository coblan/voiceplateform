from django.shortcuts import render

# Create your views here.
def voice_test(request):
    return render(request,'part3/voice_test.html',context={})