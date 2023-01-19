from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return HttpResponse("Hello world")


@login_required(login_url='login')
def home_page(request):
    return render(request, 'home.html')


def signup_page(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        uname = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Passwords do not match!!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':
        usname = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(request, username=usname, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!!")
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('login')
