from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from ..forms.school_form import SchoolForm 
from ..models.school_model import SchoolModel
from ..models.app_settings_model import AppSettingModel


# Create your views here.

@login_required(login_url='user:login')
def list_school(request):

    school_list =  SchoolModel.objects.filter(status=True)

    context = { 
        'schools': school_list
    }
    return render(request, "school/list.html", context) 


def add_school(request):

    context = {
        'title': 'Ajouter une Ecole',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Ecole',
    }

    if request.method == "POST":
        form = SchoolForm(request.POST)
        app_setting = AppSettingModel.objects.first()
        if form.is_valid():
            form = form.save(commit=False)
            form.app_settings = app_setting
            form.save()
            messages.success(request, "Ecole ajouté avec succès !")
            return redirect("dashboard:index")
        else:
            messages.error(request, "Erreur lors de l'enregistrement, veuillez vérifier les champs !")
    else:
        form = SchoolForm()
    context['form'] = form

    app_setting = AppSettingModel.objects.first()
    school = SchoolModel.objects.first()
    if not app_setting:
        return redirect('setting:add_setting')
    elif not school:
        return render(request, "school/form.html", context)
    else :
        return redirect('dashboard:index')   


@login_required(login_url='user:login')
def edit_school(request):

    context = {
        'title': 'Modifier Ecole',
        'submit_value': 'Modifier',
        'h1': 'Modifier Ecole',
    }

    school = SchoolModel.objects.first()

    if request.method == "POST":
        school_form = SchoolForm(request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            messages.success(request, "Ecole modifiée avec succès !")
            return redirect("dashboard:index")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    school_form = SchoolForm(instance=school)
    context['form'] = school_form

    return render(request, "school/form.html", context) 


@login_required(login_url='user:login')
def delete_school(request, id):
    
    school = get_object_or_404(SchoolModel, id=id)
    school.status = False
    school.save()
    messages.success(request, "Ecole suprimée avec succès !")
    return redirect('school:list_school') 


def check_school(request):

    schools = SchoolModel.objects.all()
    return redirect('dashboard:index') if schools else redirect('school:add_school')
