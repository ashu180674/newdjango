from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('this is my webpage')

def about(request) :
    return HttpResponse('about this page')
def services(request):
    return HttpResponse('at your service')