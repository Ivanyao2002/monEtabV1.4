from django.contrib import admin
from .models.absence import AbsenceModel
from .models.school import SchoolModel
from .models.student_cards import StudentCardsModel
from .models.student import StudentModel
from .models.teacher import TeacherModel


# Register your models here.
admin.site.register(AbsenceModel)
admin.site.register(SchoolModel)
admin.site.register(StudentCardsModel)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)