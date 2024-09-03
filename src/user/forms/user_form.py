from django.contrib.auth.forms import UserCreationForm
from user.models.user_model import UserModel


class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'school', 'role']

        labels = {
            'username': 'Nom d\'utilisateur',
            'school': 'Nom de l\'école',
            'role': 'Rôle',
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