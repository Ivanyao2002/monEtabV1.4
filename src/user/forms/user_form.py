from typing import Any, Mapping
from django.contrib.auth.forms import UserCreationForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from user.models.user_model import UserModel
from user.models.role_user_model import RoleUserModel
from school.models.school_model import SchoolModel
from django import forms


class UserForm(forms.ModelForm):
    password2 = forms.CharField(
        label='Confirmez le mot de passe', 
        widget=forms.PasswordInput,
        help_text='Entrez le même mot de passe que ci-dessus, pour vérification.'
    )
    class Meta:
        model = UserModel
        fields = ['username', 'school', 'role', 'password', 'password2']

        labels = {
            'username': 'Nom d\'utilisateur',
            'school': 'Nom de l\'école',
            'role': 'Rôle',
            'password': 'Mot de passe'
        }

        widgets = {
            'password': forms.PasswordInput()
        }

        help_texts = {
            'username': 'Obligatoire. 150 caractères ou moins. Lettres, chiffres et @/./+/-/_ seulement.',
            'school': 'Entrez le nom de l\'école.',
            'role': 'Sélectionnez votre rôle.',
            'password':'Votre mot de passe doit contenir au moins 8 caractères, des chiffres et des lettres',
        }

        error_messages = {
            'username': {
                'required': 'Le nom d\'utilisateur est requis.',
                'max_length': 'Le nom d\'utilisateur ne peut pas dépasser 150 caractères.',
                'unique': 'Ce nom d\'utilisateur existe déjà !!'
            },
            'password': {
                'required': 'Le mot de passe est requis.',
                'min_length': 'Le mot de passe doit contenir au moins 8 caractères.',
            },
        }
    
    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        if password1 and len(password1) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"]) 
        if commit:
            user.save()
            user.role.set(self.cleaned_data.get('role', []))
        return user
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['role'].queryset = RoleUserModel.objects.filter(status=True).exclude(role='ADMINISTRATEUR')
        self.fields['school'].queryset = SchoolModel.objects.filter(status=True)
