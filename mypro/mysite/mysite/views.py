from django.http import HttpResponse
def index(requset):
    return HttpResponse('hello')