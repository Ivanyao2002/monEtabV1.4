from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserModel(AbstractUser):

    school = models.ForeignKey("school.SchoolModel", on_delete=models.CASCADE)  
    role = models.ManyToManyField("user.RoleUserModel")

    def __str__(self):
        return f"{self.username}"    

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"