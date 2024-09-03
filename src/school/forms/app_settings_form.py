from django import forms
from ..models.app_settings_model import AppSettingModel


class AppSettingForm(forms.ModelForm):

    class Meta:
        model = AppSettingModel
        fields = ['smtp_server', 'smtp_port', 'smtp_username', 'smtp_password']

        widgets ={
            'smtp_password': forms.PasswordInput()
        }