from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from ..forms.student_form import StudentForm 
from ..models.student_model import StudentModel
from user.forms.user_form import UserForm
from user.models.user_model import UserModel


# Create your views here.

@login_required(login_url='user:login')
def list_student(request):
    

    student_list =  StudentModel.objects.filter(status=True, active=True)

    context = {
        'students': student_list
    }
    return render(request, "student/list.html", context) 


@login_required(login_url='user:login')
def add_student(request):
    context = {
        'title': 'Ajouter un Elève',
        'submit_value': 'Ajouter',
        'h1': 'Nouvel Elève',
    }

    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        # user_form = UserForm(request.POST)
        if student_form.is_valid():
            student_instance = student_form.save(commit=False)
            student_instance.active = True
            student_instance.save()
            # user_instance = user_form.save(commit=False)
            # user_instance.student = student_instance
            # user_instance.save()
            messages.success(request, 'L\'élève a été ajouté avec succès.')
            return redirect("student:list_student")
        else:
            print('erreur')
    else:
        student_form = StudentForm()
        # user_form = UserForm()
    context['form'] = student_form
    # context['forms'] = user_form

    return render(request, "student/form.html", context) 


@login_required(login_url='user:login')
def edit_student(request, id):

    student = StudentModel.objects.get(id = id)
    # user = get_object_or_404(UserModel, student=student)
    context = {
        'title': 'Modifier l\'Elève',
        'submit_value': 'Modifier',
        'h1': 'Modifier Elève',
    }
    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)
        # user_form = UserForm(request.POST, instance=user)
        if student_form.is_valid():
            student_form.save()
            # user_form.save()
            return redirect("student:list_student")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    student_form = StudentForm(instance=student)
    # user_form = UserForm(instance=user)
    context['form'] = student_form
    # context['forms'] = user_form

    return render(request, "student/form.html", context) 


@login_required(login_url='login')
def delete_student(request, id):
    student = get_object_or_404(StudentModel, id=id)
    # user = get_object_or_404(UserModel, student=student)
    student.status = False
    student.active = False
    student.save()
    # user.is_active = False
    # user.save()

    return redirect('student:list_student') 