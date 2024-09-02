from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from ..models.user import UserModel


# Create your views here.

def sign_in(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.GET.get('next', '') 
            if next:
                return redirect(next)
            else:
                return redirect('dashboard:index')

        else:
            messages.error(request, 'Veuillez verifier vos identifiants')

    return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '') 
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if not username or not password or not password2 or password != password2:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
            return render(request, 'auth/register.html')
        
        else:
            user = UserModel(username= username)
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('dashboard:index')

    return render(request, 'auth/register.html')


def log_out(request):
    logout(request)
    return redirect('user:login')   