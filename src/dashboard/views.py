from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models.user_model import UserModel
from teacher.models.teacher_model import TeacherModel
from school.models.school_model import SchoolModel
from student.models.student_model import StudentModel
from student.models.student_cards_model import StudentCardsModel
from student.models.absence_model import AbsenceModel


# Create your views here.
@login_required(login_url='user:login')
def index(request):

    all_users = UserModel.objects.filter(is_active=True).count()
    all_teachers = TeacherModel.objects.filter(status=True).count()
    all_schools = SchoolModel.objects.filter(status=True).count()
    all_students = StudentModel.objects.filter(status=True).count()
    all_student_cards = StudentCardsModel.objects.filter(status=True).count()
    all_absences = AbsenceModel.objects.filter(status=True).count()
    all_students_man = StudentModel.objects.filter(gender='H', status=True).count()
    all_students_woman = StudentModel.objects.filter(gender='F', status=True).count()
    all_students_other = StudentModel.objects.filter(gender='O', status=True).count()

    context = {
        'all_users': all_users,
        'all_teachers': all_teachers,
        'all_students': all_students, 
        'all_schools': all_schools, 
        'all_student_cards': all_student_cards, 
        'all_absences': all_absences, 
        'all_students_man': all_students_man,
        'all_students_woman': all_students_woman,
        'all_students_other': all_students_other,
    }    

    return render(request, 'dashboard/index.html', context)
