from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here
def frontend_index(request):
    return HttpResponse("this is frontend")

def registration(request):
    if request.user.is_authenticated:
        return render(request, 'backend/index.html')
    else:
        fm = CreateUserForm()
        if request.method == 'POST':
            fm = CreateUserForm(request.POST)
            if fm.is_valid():
                fm.save()
                username = fm.cleaned_data.get('username')
                messages.success(request, "Account Created success by " + username)
                return redirect('login')
            else:
                messages.error(request, 'All Field is required')
                return redirect('register') 
            
        
        return render(request, 'backend/user_auth/registration.html')


def login_page(request):
    if request.user.is_authenticated:
        return render(request, 'backend/index.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username and password does not match!')
                return redirect('login')
                
        return render(request, 'backend/user_auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    