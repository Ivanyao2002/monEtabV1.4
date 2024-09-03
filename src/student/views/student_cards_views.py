from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from ..forms.student_cards_form import StudentCardForm 
from ..models.student_cards_model import StudentCardsModel


# Create your views here.

@login_required(login_url='user:login')
def list_student_card(request):

    student_card_list =  StudentCardsModel.objects.filter(status=True)

    context = {
        'student_cards': student_card_list
    }
    return render(request, "student_cards/list.html", context) 


@login_required(login_url='user:login')
def add_student_card(request):
    context = {
        'title': 'Ajouter une Carte élève',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Carte',
    }

    if request.method == "POST":
        form = StudentCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_cards:list_student_card")
        else:
            print('erreur')
    else:
        form = StudentCardForm()
    context['form'] = form

    return render(request, "student_cards/form.html", context) 


@login_required(login_url='user:login')
def edit_student_card(request, id):

    student_card = StudentCardsModel.objects.get(id = id)
    context = {
        'title': 'Modifier la carte',
        'submit_value': 'Modifier',
        'h1': 'Modifier Carte Eleve',
    }
    if request.method == "POST":
        student_card_form = StudentCardForm(request.POST, instance=student_card)
        if student_card_form.is_valid():
            student_card_form.save()
            return redirect("student_cards:list_student_card")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    student_card_form = StudentCardForm(instance=student_card)
    context['form'] = student_card_form

    return render(request, "student_cards/form.html", context) 


@login_required(login_url='user:login')
def delete_student_card(request, id):
    student_card = get_object_or_404(StudentCardsModel, id=id)
    # student_card.delete()
    student_card.status = False
    student_card.save()
    return redirect('student_cards:list_student_card') 