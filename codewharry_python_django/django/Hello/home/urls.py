from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "clour Admin"
admin.site.site_title = "clour Admin Portal"
admin.site.index_title = "Welcome to clour Researcher Portal"

urlpatterns = [
    path('sendhelp', views.sendhelp, name='sendhelp'),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('shirt', views.shirt, name='shirt'),
    path('cargos', views.cargos, name='cargos'),
    path('accessories', views.accessories, name='accessories'),
    
]