from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
# password for test user is 8I68008$69 and username is croma

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html') 


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # correct credentials 
        user = authenticate(username=username, password=password)
        if user is not None:
            # print("user logged in")
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

    
def logout_user(request):
    print("Logout function called")  # Add this print statement
    logout(request)  # Call Django's logout function
    return redirect("/login")