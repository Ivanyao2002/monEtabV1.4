from django.contrib import admin
from .models.absence_model import AbsenceModel
from .models.student_cards_model import StudentCardsModel
from .models.student_model import StudentModel


# Register your models here.

admin.site.register(StudentModel)
admin.site.register(AbsenceModel)
admin.site.register(StudentCardsModel)