from django.db import models
from django.utils.translation import gettext_lazy as _
from .date_time_model import DateTimeModel
from ..gender_ennum import GenderEnum


# Create your models here.

class PersonModel(DateTimeModel):

    user = models.OneToOneField('user.UserModel', on_delete=models.SET_NULL, null=True) 
    address = models.OneToOneField('base.AdressModel', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30, verbose_name="Nom ")
    last_name = models.CharField(max_length=60, verbose_name="Prénoms ")
    gender = models.CharField(max_length=1, choices=GenderEnum.choices, default=GenderEnum.MALE, verbose_name="Genre ")
    birthday = models.DateField(verbose_name="Date de naissance ") 
    phone_number = models.CharField(max_length=15, verbose_name="Téléphone ")
    url_picture = models.CharField(max_length=255, verbose_name="Lien de l'image ")
    active = models.BooleanField(default=False, verbose_name="Actif ")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    
