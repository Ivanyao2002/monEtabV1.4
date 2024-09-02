from django import forms
from .models.adress import AdressModel


class AdressForm(forms.ModelForm):

    class Meta:
        model = AdressModel
        fields = ['student', 'teacher', 'city', 'street', 'country']


        labels ={
            'student': 'Nom de l\'élève',
            'teacher': 'Nom du professeur',
        }