from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserModel(AbstractUser):

    school = models.ForeignKey("school.SchoolModel", on_delete=models.CASCADE, null=True)  
    role = models.ForeignKey("user.RoleUserModel", on_delete=models.SET_NULL, null=True)
    # pseudo = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username}"    

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"