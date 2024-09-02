from django import forms
from .models.app_setting import AppSettingModel


class AppSettingForm(forms.ModelForm):

    class Meta:
        model = AppSettingModel
        fields = ['school', 'smtp_server', 'smtp_port', 'smtp_username', 'smtp_password']

        widgets ={
            'smtp_password': forms.PasswordInput()
        }