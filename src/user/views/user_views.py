from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from ..models.user_model import UserModel
from ..models.role_user_model import RoleUserModel
from ..forms.user_form import UserForm
from school.models.app_settings_model import AppSettingModel
from school.models.school_model import SchoolModel


# Create your views here.

def sign_in(request):

    if request.user.is_authenticated:
        messages.success(request, 'Vous êtes déjà connecté !!')
        return redirect('dashboard:index')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion Réussie !!')
            return redirect(next_url if next_url else 'dashboard:index')
        else:
            messages.error(request, 'Veuillez verifier vos identifiants')    
    
    users = UserModel.objects.all()
    app_settings = AppSettingModel.objects.all()
    schools = SchoolModel.objects.all()

    if not app_settings:
        return redirect('setting:add_setting')
    elif not schools:
        return redirect('school:add_school')
    elif not users:
        return redirect('user:register')
    return render(request, 'auth/login.html')


def register(request):

    user_admin = UserModel.objects.filter(is_superuser=True, is_staff=True)

    if user_admin:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST.get('username', '') 
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        role_name = 'ADMINISTRATEUR' 
        if not username or not password or not password2:
            messages.error(request, "Veuillez vérifier les champs ! Tous les champs doivent être remplis !")
            return render(request, 'auth/register.html')
        
        if password != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'auth/register.html')

        if len(password) < 8:
            messages.error(request, "Le mot de passe doit contenir plus de 08 caractères.")
            return render(request, 'auth/register.html')
        
        if UserModel.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà !!")
            return render(request, 'auth/register.html')
        
        users = UserModel.objects.all()

        if not users:
        
            role_user, created_at = RoleUserModel.objects.get_or_create(role=role_name) # On recupère le rôle de user si il existe déjà, sinon on crée un nouveau parce que role est le pk
            
            user = UserModel(username= username)
            user.set_password(password)
            user.school = SchoolModel.objects.first()
            user.is_superuser = True
            user.is_staff = True
            user.save() # On enregistre l'utilisateur pour recuperer son id 
            user.role.add(role_user) # On ajoute le role; Il faut que les deux modèles aient des id pour que la relation many-to-many soit utilisé. la méthode add permet d'établir le lien
            login(request, user)
            messages.success(request, "Compte créer avec succès !!")
            return redirect('dashboard:index')
        else:
            return redirect('user:login')

    app_setting = AppSettingModel.objects.first()
    school = SchoolModel.objects.all()
    if not app_setting:
        return redirect('setting:add_setting')
    elif not school:
        return redirect('school:add_school')
    return render(request, 'auth/register.html')


def log_out(request):

    logout(request)
    messages.success(request, 'Vous êtes bien déconnecté !!')
    return redirect('user:login')  

 
@login_required(login_url='user:login')
def list_user(request):

    context = {}
    search_field = request.GET.get('search')
    if search_field:
        users = UserModel.objects.filter(username__icontains=search_field, is_active=True)
        context['users'] = users
        context['search_field'] = search_field
    else:
        user_list =  UserModel.objects.all()
        context['users'] = user_list

    # context = {
    #     'users': user_list
    # }
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
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Compte Utilisateur ajouté avec succès !')
            return redirect('user:list_user')
        else:
            messages.error(request, "Erreur lors de l'enregistrement, veuillez vérifier les champs !")
    else:
        user_form = UserForm()
    context['form'] = user_form

    return render(request, "user/form.html", context) 
 

@login_required(login_url='login')
def edit_user(request, id):

    context = {
        'title': 'Modifier l\'utilisateur',
        'submit_value': 'Modifier',
        'h1': 'Modifier Utilisateur',
    }

    user = UserModel.objects.get(id = id)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Compte Utilisateur modifié !")
            return redirect("user:list_user")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    user_form = UserForm(instance=user)
    context['form'] = user_form

    return render(request, "user/form.html", context) 
 

@login_required(login_url='login')
def deactivate_user(request, id):

    user = get_object_or_404(UserModel, id=id)
    user.is_active = False
    user.save()
    messages.success(request, "Compte Utilisateur désactivé !")
    return redirect('user:list_user') 


@login_required(login_url='login')
def activate_user(request, id):

    user = get_object_or_404(UserModel, id=id)
    user.is_active = True
    user.save()
    messages.success(request, "Compte Utilisateur activé !")
    return redirect('user:list_user') 