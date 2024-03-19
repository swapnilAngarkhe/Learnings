from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import About
from django.contrib import messages


# Create your views here.

def sendhelp(request):
    return HttpResponse('roses are red, the sun is shining my mental health is declining')

def index(request):
    # return HttpResponse('this is a homepage')
    
    context={
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse('about page')
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        about= About(name=name, email=email, phone=phone, desc=desc, date=datetime.now() )
        about.save()
        messages.success(request, "Your message has been sent.")
    
    return render(request, 'about.html')

def shirt(request):
    # return HttpResponse('shirt page')
    return render(request, 'shirt.html')

def cargos(request):
    # return HttpResponse('cargo page')
    return render(request, 'cargos.html')

def accessories(request):
    return render(request, 'accessories.html')