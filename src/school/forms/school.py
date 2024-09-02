from django import forms
from ..models.school import SchoolModel


class SchoolForm(forms.ModelForm):

    class Meta:
        model = SchoolModel
        fields = ['name', 'url_logo']

        labels ={
            'name': "Nom de l'école"
        }   