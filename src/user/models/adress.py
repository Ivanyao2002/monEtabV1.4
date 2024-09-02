from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class AdressModel(DateTimeModel):

    student = models.OneToOneField("school.StudentModel", on_delete=models.CASCADE, blank=True, null=True, related_name="adress_student_ids")
    teacher = models.OneToOneField("school.TeacherModel", on_delete=models.CASCADE, blank=True, null=True, related_name="adress_teacher_ids")
    city = models.CharField(max_length=50, verbose_name="Ville ")  
    street = models.CharField(max_length=50, verbose_name="Quartier ")  
    country = models.CharField(max_length=50, verbose_name="Pays ")  


    def __str__(self):
        return f"{self.country} - {self.city} - {self.street}"    

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"