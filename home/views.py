from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    context = {
        "variable1" : "this is ashu",
        "variable2":"this is v2"    
    } 
                        
    return render(request,'index.html', context)

def aboutus(request) :
    return render(request,'aboutus.html')

def services(request):
    return render(request,'services.html')

def contactus(request):
    return render(request,'contactus.html')

def icecream(request):
    return render(request,'icecream.html')

def home(request) :
    return render(request,'home.html')