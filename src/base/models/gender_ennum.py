from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class GenderEnum(models.TextChoices):
    
    MEN  = "Homme", _("Homme")
    WOMEN  = "Femme", _("Femme")
    OTHER  = "Autre", _("Autre")