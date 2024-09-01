from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

from ..models.teacher import TeacherModel

# Create your views here.
# @login_required(login_url='login')
def list_teacher(request):

    teacher_list =  TeacherModel.objects.all()

    paginator = Paginator(teacher_list, 10)  
    page_number = request.GET.get('page')
    teachers = paginator.get_page(page_number)

    context = {
        'teachers': teachers
    }
    return render(request, "teacher/list.html", context) 


# @login_required(login_url='login')
def add_teacher(request):
    context = {
        'title': 'Ajouter professeur',
        'submit_value': 'Ajouter'
    }

    # if request.method == "POST":
    #     form = TeacherForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Le professeur a été ajouté avec succès.")
    #         return redirect("teacher:index")
    #     else:
    #         print('erreur')
    #         messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
    # else:
    #     form = TeacherForm()
    # context['form'] = form

    return render(request, "teacher/form.html", context) 
 

# @login_required(login_url='login')
# def update_teacher(request, id):

#     teacher = TeacherModel.objects.get(id = id)
#     context = {
#         'title': 'Modifier le professeur',
#         'submit_value': 'Modifier'
#     }
#     if request.method == "POST":
#         teacher_form = TeacherForm(request.POST, instance=teacher)
#         if teacher_form.is_valid():
#             teacher_form.save()
#             return redirect("teacher:index")
#         else:
#             print("formulaire erroné")
#             messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


#     teacher_form = TeacherForm(instance=teacher)
#     context['form'] = teacher_form

#     return render(request, "teacher/add_teacher.html", context) 
 

# @login_required(login_url='login')
# def delete_teacher(request, id):
    teacher = get_object_or_404(TeacherModel, id=id)
    teacher.delete()

    return redirect('teacher:index') 