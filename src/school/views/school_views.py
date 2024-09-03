from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from ..forms.school_form import SchoolForm 
from ..models.school_model import SchoolModel


# Create your views here.

@login_required(login_url='user:login')
def list_school(request):

    school_list =  SchoolModel.objects.filter(status=True)

    context = { 
        'schools': school_list
    }
    return render(request, "school/list.html", context) 


@login_required(login_url='user:login')
def add_school(request):
    context = {
        'title': 'Ajouter une Ecole',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Ecole',
    }

    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("school:list_school")
        else:
            print('erreur')
    else:
        form = SchoolForm()
    context['form'] = form

    return render(request, "school/form.html", context) 


@login_required(login_url='user:login')
def edit_school(request, id):

    school = SchoolModel.objects.get(id = id)
    context = {
        'title': 'Modifier Ecole',
        'submit_value': 'Modifier',
        'h1': 'Modifier Ecole',
    }
    if request.method == "POST":
        school_form = SchoolForm(request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            return redirect("school:list_school")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    school_form = SchoolForm(instance=school)
    context['form'] = school_form

    return render(request, "school/form.html", context) 


@login_required(login_url='user:login')
def delete_school(request, id):
    school = get_object_or_404(SchoolModel, id=id)
    # school.delete()
    school.status = False
    school.save()
    return redirect('school:list_school') 