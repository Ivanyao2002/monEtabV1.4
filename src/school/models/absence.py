from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class AbsenceModel(DateTimeModel):

    student = models.ForeignKey("school.StudentModel", on_delete=models.CASCADE, related_name="absence_student_ids")
    absence_date = models.DateField(verbose_name="Date de l'absence ")  
    absence_number = models.IntegerField(verbose_name="Nombre d'absence ")  


    def __str__(self):
        return f"{self.absence_date} - {self.absence_number}"    

    class Meta:
        verbose_name = "Absence"
        verbose_name_plural = "Absences"