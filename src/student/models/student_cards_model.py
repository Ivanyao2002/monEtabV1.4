from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class StudentCardsModel(DateTimeModel):

    student = models.ForeignKey("student.StudentModel", on_delete=models.CASCADE)
    issue_date = models.DateField(verbose_name="Date d'issue ")  
    reference = models.CharField(max_length=50, verbose_name="Référence ")  
    expiration_date = models.DateField(verbose_name="Date d'expiration ")   


    def __str__(self):
        return f"{self.reference} - {self.expiration_date}"    

    class Meta:
        verbose_name = "Carte Etudiant"
        verbose_name_plural = "Cartes Etudiant"
