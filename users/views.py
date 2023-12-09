from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def signup_view(request):
    return render(request, 'signup.html')



def userSuccess(request):
    print("Hit korse")
    if request.user.is_authenticated:
        username = request.user.username
        userCreate =  Profile.objects.create(user=request.user)
        if userCreate[1] == True:
            print('user created'+ username)
    pass

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('home')