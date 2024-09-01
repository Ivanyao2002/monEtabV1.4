from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.

class SchoolModel(NamedDateTimeModel):

    url_logo = models.CharField(max_length=50, verbose_name="Lien du logo ")


    def __str__(self):
        return f"{self.name}"    

    class Meta:
        verbose_name = "Ecole"
        verbose_name_plural = "Ecoles"
