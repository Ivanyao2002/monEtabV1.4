from django import forms
from ..models.adress_model import AdressModel


class AdressForm(forms.ModelForm):

    class Meta:
        model = AdressModel
        fields = ['city', 'street', 'country']
