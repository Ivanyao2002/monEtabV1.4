from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from ..models.teacher import TeacherModel
from ..forms.teacher import TeacherForm, UserForm 
from user.models.user import UserModel

# Create your views here.
@login_required(login_url='user:login')
def list_teacher(request):

    teacher_list =  TeacherModel.objects.filter(status=True, active=True)

    context = {
        'teachers': teacher_list
    }
    return render(request, "teacher/list.html", context) 


@login_required(login_url='user:login')
def add_teacher(request):
    context = {
        'title': 'Ajouter un Professeur',
        'submit_value': 'Ajouter',
        'h1': 'Nouveau Professeur',
    }

    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        user_form = UserForm(request.POST)
        if teacher_form.is_valid() and user_form.is_valid():
            teacher_instance = teacher_form.save()
            user_instance = user_form.save(commit=False)
            user_instance.teacher = teacher_instance
            user_instance.save()
            messages.success(request, 'Le professeur a été ajouté avec succès.')
            return redirect('teacher:list_teacher')
        else:
            print(teacher_form.errors)
            print(user_form.errors)
    else:
        teacher_form = TeacherForm()
        user_form = UserForm()
    context['form'] = teacher_form
    context['forms'] = user_form

    return render(request, "teacher/form.html", context) 
 

@login_required(login_url='login')
def edit_teacher(request, id):

    teacher = TeacherModel.objects.get(id = id)
    user = get_object_or_404(UserModel, teacher=teacher)
    context = {
        'title': 'Modifier le professeur',
        'submit_value': 'Modifier',
        'h1': 'Modifier Professeur',
    }
    if request.method == "POST":
        teacher_form = TeacherForm(request.POST, instance=teacher)
        user_form = UserForm(request.POST, instance=user)
        if teacher_form.is_valid() and user_form.is_valid():
            teacher_form.save()
            user_form.save()
            return redirect("teacher:index")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    teacher_form = TeacherForm(instance=teacher)
    user_form = UserForm(instance=user)
    context['form'] = teacher_form
    context['forms'] = user_form

    return render(request, "teacher/form.html", context) 
 

@login_required(login_url='login')
def delete_teacher(request, id):
    teacher = get_object_or_404(TeacherModel, id=id)
    user = get_object_or_404(UserModel, teacher=teacher)
    teacher.status = False
    teacher.active = False
    teacher.save()
    user.is_active = False
    user.save()

    return redirect('teacher:list_teacher') 