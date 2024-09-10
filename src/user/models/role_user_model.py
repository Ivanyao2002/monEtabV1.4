from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class RoleUserModel(DateTimeModel):

    role = models.CharField(max_length=150, verbose_name="Rôle de l'utilisateur ", primary_key=True)

    def __str__(self):
        return f"{self.role}"    

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"