from django.shortcuts import render


#create your views here

def index():
    return render(request, "newyear/index.html" ,{
        "newyear"
    }
    )