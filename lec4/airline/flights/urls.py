from . import views 
from django.urls import path, include

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:flight_id>", views.flight, name='flight'),
]