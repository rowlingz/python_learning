from django.http import HttpResponse
import json

def hello(request) :
    return HttpResponse('周宁！我爱你。。。。')