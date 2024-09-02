from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from ..forms.absence import AbsenceForm 
from ..models.absence import AbsenceModel


# Create your views here.

@login_required(login_url='user:login')
def list_absence(request):

    absence_list =  AbsenceModel.objects.filter(status=True)

    context = {
        'absences': absence_list
    }
    return render(request, "absence/list.html", context) 


@login_required(login_url='user:login')
def add_absence(request):
    context = {
        'title': 'Ajouter une Absence',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Absence',
    }

    if request.method == "POST":
        form = AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("absence:list_absence")
        else:
            print('erreur')
    else:
        form = AbsenceForm()
    context['form'] = form

    return render(request, "absence/form.html", context) 


@login_required(login_url='user:login')
def edit_absence(request, id):

    absence = AbsenceModel.objects.get(id = id)
    context = {
        'title': 'Modifier l\'Absence',
        'submit_value': 'Modifier',
        'h1': 'Modifier Absence',
    }
    if request.method == "POST":
        absence_form = AbsenceForm(request.POST, instance=absence)
        if absence_form.is_valid():
            absence_form.save()
            return redirect("absence:list_absence")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    absence_form = AbsenceForm(instance=absence)
    context['form'] = absence_form

    return render(request, "absence/form.html", context) 


@login_required(login_url='user:login')
def delete_absence(request, id):
    absence = get_object_or_404(AbsenceModel, id=id)
    absence.status = False
    absence.save()
    return redirect('absence:list_absence') 