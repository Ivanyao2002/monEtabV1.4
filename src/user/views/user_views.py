from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from ..models.user_model import UserModel
from ..forms.user_form import UserForm


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

 
@login_required(login_url='user:login')
def list_user(request):

    user_list =  UserModel.objects.filter(is_active=True)

    context = {
        'users': user_list
    }
    return render(request, "user/list.html", context) 


@login_required(login_url='user:login')
def add_user(request):
    context = {
        'title': 'Ajouter un Utilisateur',
        'submit_value': 'Ajouter',
        'h1': 'Nouvel Utilisateur', 
    }

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid() and user_form.is_valid():
            user_form.save()
            messages.success(request, 'L\'utilisateur a été ajouté avec succès.')
            return redirect('user:list_user')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    context['form'] = user_form

    return render(request, "user/form.html", context) 
 

@login_required(login_url='login')
def edit_user(request, id):

    user = UserModel.objects.get(id = id)
    context = {
        'title': 'Modifier l\'utilisateur',
        'submit_value': 'Modifier',
        'h1': 'Modifier Utilisateur',
    }
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect("user:list_user")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    user_form = UserForm(instance=user)
    context['form'] = user_form

    return render(request, "user/form.html", context) 
 

@login_required(login_url='login')
def delete_user(request, id):

    user = get_object_or_404(UserModel, id=id)
    user.is_active = False
    user.save()

    return redirect('user:list_user') 