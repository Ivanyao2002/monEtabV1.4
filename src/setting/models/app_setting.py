from django.db import models 
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class AppSettingModel(DateTimeModel):

    school = models.OneToOneField("school.SchoolModel", on_delete=models.CASCADE, related_name="app_setting_school_ids", verbose_name="Ecole")
    smtp_server = models.CharField(max_length=50, verbose_name="Server SMTP ")
    smtp_port = models.IntegerField(verbose_name="Port SMTP ")
    smtp_username = models.CharField(max_length=50, verbose_name="Nom d'utilisateur SMTP ")
    smtp_password = models.CharField(max_length=128, verbose_name="Mot de passe SMTP ")


    def __str__(self):
        return f"{self.smtp_server} - {self.smtp_username}"    

    class Meta:
        verbose_name = "Paramètre appli"
        verbose_name_plural = "Paramètre appli"