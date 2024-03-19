from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.logout_user, name="logout_user"),

]
