from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class RoleUserModel(DateTimeModel):

    user = models.ForeignKey("user.UserModel", on_delete=models.CASCADE, related_name="role_user_user_ids")
    role = models.CharField(max_length=255, verbose_name="Rôle de l'utilisateur ")

    def __str__(self):
        return f"{self.role}"    

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"