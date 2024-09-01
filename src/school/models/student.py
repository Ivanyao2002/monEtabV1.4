from django.db import models
from base.models.person import PersonModel


# Create your models here.

class StudentModel(PersonModel):

    user_id = models.OneToOneField("user.UserModel", on_delete=models.CASCADE, related_name="student_user_ids")
    adress_id = models.OneToOneField("user.AdressModel", on_delete=models.CASCADE, related_name="student_adress_ids")
    matricule = models.CharField(max_length=50, verbose_name="Matricule ")  
    phone_number_father = models.CharField(max_length=15, verbose_name="Téléphone du père ")  


    def __str__(self):
        return f"{self.matricule} - {self.first_name}"    

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"