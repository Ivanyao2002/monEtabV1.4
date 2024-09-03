from django.db import models
from .helpers.date_time_model import DateTimeModel


class AdressModel(DateTimeModel):

    city = models.CharField(max_length=50, verbose_name="Ville ")  
    street = models.CharField(max_length=50, verbose_name="Quartier ")  
    country = models.CharField(max_length=50, verbose_name="Pays ")  


    def __str__(self):
        return f"{self.country} - {self.city} - {self.street}"    

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"