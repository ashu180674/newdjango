from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    context = {
        "variable1" : "this is ashu",
        "variable2":"this is v2"    
    } 
                        
    return render(request,'index.html', context)

def aboutus(request) :
    return HttpResponse('about this page')
def services(request):
    return HttpResponse('at your service')

def contactus(request):
    return HttpResponse("dail +916232296539")

def icecream(request):
    return render(request,'icecream.html')