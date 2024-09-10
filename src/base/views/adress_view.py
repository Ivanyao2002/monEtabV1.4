from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from ..forms.adress_form import AdressForm
from ..models.adress_model import AdressModel


# Create your views here.

@login_required(login_url='user:login')
def list_adress(request):

    adress_list =  AdressModel.objects.filter(status=True)

    context = {
        'adresses': adress_list
    }
    return render(request, "adress/list.html", context) 


@login_required(login_url='user:login')
def add_adress(request):

    context = {
        'title': 'Ajouter une Adresse',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Adresse',
    }

    if request.method == "POST":
        form = AdressForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Adresse ajoutée avec succès !")
            return redirect("adress:list_adress")
        else:
            messages.error(request, "Erreur lors de l'enregistrement, veuillez vérifier les champs !")
    else:
        form = AdressForm()
    context['form'] = form

    return render(request, "adress/form.html", context) 


@login_required(login_url='user:login')
def edit_adress(request, id):

    adress = AdressModel.objects.get(id = id)
    context = {
        'title': 'Modifier l\'Adresse ',
        'submit_value': 'Modifier',
        'h1': 'Modifier Adresse',
    }
    if request.method == "POST":
        adress_form = AdressForm(request.POST, instance=adress)
        if adress_form.is_valid():
            adress_form.save()
            messages.success(request, "Adresse modifiée avec succès !")
            return redirect("adress:list_adress")
        else:
            messages.error(request, "Erreur dans le formulaire ! Veuillez vérifier les champs !")

    adress_form = AdressForm(instance=adress)
    context['form'] = adress_form

    return render(request, "adress/form.html", context) 


@login_required(login_url='user:login')
def delete_adress(request, id):

    adress = get_object_or_404(AdressModel, id=id)
    adress.status = False
    adress.save()
    messages.success(request, "Adresse suprimée avec succès !")
    return redirect('adress:list_adress') 