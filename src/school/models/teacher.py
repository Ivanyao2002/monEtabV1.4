from django.db import models
from base.models.person import PersonModel


# Create your models here.

class TeacherModel(PersonModel):

    user_id = models.OneToOneField("user.UserModel", on_delete=models.CASCADE, related_name="teacher_user_ids")
    adress_id = models.OneToOneField("user.AdressModel", on_delete=models.CASCADE, related_name="teacher_adress_ids")
    available = models.CharField(default=True, verbose_name="Disponible ")  
    speciality = models.CharField(max_length=50, verbose_name="Spécialité ")  


    def __str__(self):
        return f"{self.first_name} - {self.speciality} - {self.available}"    

    class Meta:
        verbose_name = "Professeur"
        verbose_name_plural = "Professeurs"