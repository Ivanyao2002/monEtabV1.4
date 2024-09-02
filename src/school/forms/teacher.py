from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models.teacher import TeacherModel
from user.models.user import UserModel


class TeacherForm(forms.ModelForm):

    class Meta:
        model = TeacherModel
        exclude = ['status', 'active']

        widgets ={
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2']

        labels = {
            'username': 'Nom d\'utilisateur',
            'password1': 'Mot de passe',
            'password2': 'Confirmation du mot de passe',
        }

        usable_password_help_text = (
        "Whether the user will be able to authenticate using a password or not. "
        "If disabled, they may still be able to authenticate using other backends, "
        "such as Single Sign-On or LDAP."
        )
        error_messages = {
            'password1': {'required': 'Ce champ est obligatoire.'},
            'password2': {'required': 'Ce champ est obligatoire.'},
        }