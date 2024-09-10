from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from ..forms.app_settings_form import AppSettingForm
from ..models.app_settings_model import AppSettingModel


# Create your views here.

@login_required(login_url='user:login')
def list_setting(request):

    setting_list =  AppSettingModel.objects.filter(status=True)

    context = {
        'settings': setting_list
    }
    return render(request, "setting/list.html", context) 


def add_setting(request):

    context = {
        'title': 'Ajouter un Paramètre',
        'submit_value': 'Ajouter',
        'h1': 'Nouveau Paramètre',
    }

    if request.method == "POST":
        form = AppSettingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Paramètre ajouté avec succès !")
            return redirect("school:add_school")
        else:
            messages.error(request, "Erreur lors de l'enregistrement, veuillez vérifier les champs !")
    else:
        form = AppSettingForm()
    context['form'] = form

    app_setting = AppSettingModel.objects.first()
    return render(request, "setting/form.html", context) if not app_setting else redirect('school:add_school')


@login_required(login_url='user:login')
def edit_setting(request):

    context = {
   
        'title': 'Modifier le Paramètre',
        'submit_value': 'Modifier',
        'h1': 'Modifier Paramètre',
    }

    setting = AppSettingModel.objects.first()
    
    if request.method == "POST":
        setting_form = AppSettingForm(request.POST, instance=setting)
        if setting_form.is_valid():
            setting_form.save()
            messages.success(request, "Paramètre modifié avec succès !")
            return redirect("dashboard:index")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    setting_form = AppSettingForm(instance=setting)
    context['form'] = setting_form

    return render(request, "setting/form.html", context) 


@login_required(login_url='user:login')
def delete_setting(request, id):

    setting = get_object_or_404(AppSettingModel, id=id)
    setting.status = False
    setting.save()
    messages.success(request, "Paramètre suprimé avec succès !")
    return redirect('setting:list_setting') 


def check_settings(request):
    
    app_settings = AppSettingModel.objects.all()
    return redirect('school:check_school') if app_settings else redirect('setting:add_setting')