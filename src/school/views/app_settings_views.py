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


# @login_required(login_url='user:login')
def add_setting(request):
    context = {
        'title': 'Ajouter un Paramètre',
        'submit_value': 'Ajouter',
        'h1': 'Nouveau Paramètre',
    }

    app_settings = AppSettingModel.objects.all()

    if request.method == "POST":
        form = AppSettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("school:add_school")
        else:
            print('erreur')
    else:
        form = AppSettingForm()
    context['form'] = form

    if not app_settings:
        return render(request, "setting/form.html", context) 
    else:
        return redirect('school:add_school')


@login_required(login_url='user:login')
def edit_setting(request, id):

    setting = AppSettingModel.objects.get(id = id)
    context = {
        'title': 'Modifier le Paramètre',
        'submit_value': 'Modifier',
        'h1': 'Modifier Paramètre',
    }
    if request.method == "POST":
        setting_form = AppSettingForm(request.POST, instance=setting)
        if setting_form.is_valid():
            setting_form.save()
            return redirect("setting:list_setting")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    setting_form = AppSettingForm(instance=setting)
    context['form'] = setting_form

    return render(request, "setting/form.html", context) 


@login_required(login_url='user:login')
def delete_setting(request, id):

    setting = get_object_or_404(AppSettingModel, id=id)
    # setting.delete()
    setting.status = False
    setting.save()
    return redirect('setting:list_setting') 

def check_settings(request):
    app_settings = AppSettingModel.objects.all()
    return redirect('school:check_school') if app_settings else redirect('setting:add_setting')
    # if not app_settings:
    #     return redirect('setting:add_setting')
    # else:
    #     return redirect('school:check_school')