from django.db import models
from base.models.person_model import PersonModel


# Create your models here.

class TeacherModel(PersonModel):

    available = models.BooleanField(default=True, verbose_name="Disponible ")  
    speciality = models.CharField(max_length=50, verbose_name="Spécialité ")  


    def __str__(self):
        return f"{self.first_name} - {self.speciality} - {self.available}"    

    class Meta:
        verbose_name = "Professeur"
        verbose_name_plural = "Professeurs"