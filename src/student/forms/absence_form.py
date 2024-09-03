from django import forms
from ..models.absence_model import AbsenceModel


class AbsenceForm(forms.ModelForm):

    class Meta:
        model = AbsenceModel
        fields = ['student', 'absence_date', 'absence_number'] 

        widgets ={
            'absence_date': forms.DateInput(attrs={'type': 'date'})
        }

        labels ={
            "student": "Nom de l'élève"
        }   