from django.http import HttpResponse
from django.shortcuts import render
# def index(requset):
#     return HttpResponse('hello')

def index(req):
    return render(req,'index.html',{'msg':'这是首页'})
