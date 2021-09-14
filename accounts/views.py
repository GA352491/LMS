from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect


# Create your views here.

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('email').lower()
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')

    return render(request, 'login.html')


def sign_out(request):
    logout(request)
    return redirect('login')
