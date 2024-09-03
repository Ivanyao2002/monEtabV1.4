from django import forms
from ..models.role_user_model import RoleUserModel


class RoleUserForm(forms.ModelForm):

    class Meta:
        model = RoleUserModel
        fields = ['role'] 