from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from ..forms.role_user_form import RoleUserForm 
from ..models.role_user_model import RoleUserModel


# Create your views here.

@login_required(login_url='user:login')
def list_role_user(request):

    role_user_list =  RoleUserModel.objects.filter(status=True)

    context = {
        'role_users': role_user_list
    }
    return render(request, "role_user/list.html", context) 


@login_required(login_url='user:login')
def add_role_user(request):
    context = {
        'title': 'Ajouter un Rôle Utilisateur',
        'submit_value': 'Ajouter',
        'h1': 'Nouveau Rôle ',
    }

    if request.method == "POST":
        form = RoleUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("role_user:list_role_user")
        else:
            print('erreur')
    else:
        form = RoleUserForm()
    context['form'] = form

    return render(request, "role_user/form.html", context) 


@login_required(login_url='user:login')
def edit_role_user(request, id):

    role_user = RoleUserModel.objects.get(id = id)
    context = {
        'title': 'Modifier le Rôle de l\'Utilisateur',
        'submit_value': 'Modifier',
        'h1': 'Modifier Rôle Utilisateur',
    }
    if request.method == "POST":
        role_user_form = RoleUserForm(request.POST, instance=role_user)
        if role_user_form.is_valid():
            role_user_form.save()
            return redirect("role_user:list_role_user")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    role_user_form = RoleUserForm(instance=role_user)
    context['form'] = role_user_form

    return render(request, "role_user/form.html", context) 


@login_required(login_url='user:login')
def delete_role_user(request, id):
    role_user = get_object_or_404(RoleUserModel, id=id)
    # role_user.delete()
    role_user.status = False
    role_user.save()
    return redirect('role_user:list_role_user') 