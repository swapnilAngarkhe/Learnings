from django.shortcuts import render
from . models import Flight

# Create your views here.

def index(request):
    
    context={
        "flights":Flight.objects.all()
    }
    
    return render(request, "flights/index.html",  context)

def flight(request, flight_id):
    flight=Flight.objects.get(pk=flight_id) #primary key = flightid
    return render (request, "flights/flight.html", {
        "flight":flight,
        "passengers":flight.passengers.all()
    })
    