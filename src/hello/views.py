from django.shortcuts import render,HttpResponse,Http404
import requests


# Create your views here.

def relay(request):
    url =  request.GET.get('url')
    if url:
        rt = requests.get(url)
        return HttpResponse(content=rt.content,content_type=rt.headers.get('Content-Type'))
    else:
        return Http404()