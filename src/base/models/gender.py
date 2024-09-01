from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class GenderEnum(models.TextChoices):
    
    MALE  = "H", _("Homme")
    FEMALE  = "F", _("Femme")
    OTHER  = "O", _("Autre")