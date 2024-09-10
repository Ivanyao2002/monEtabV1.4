from django import forms
from ..models.app_settings_model import AppSettingModel
from django.contrib.auth.hashers import make_password


class AppSettingForm(forms.ModelForm):

    class Meta:
        model = AppSettingModel
        fields = ['smtp_server', 'smtp_port', 'smtp_username', 'smtp_password']

        widgets ={
            'smtp_password': forms.PasswordInput()
        }

    def save(self, commit=True):
        app_setting = super().save(commit=False)
        app_setting.smtp_password = make_password(self.cleaned_data["smtp_password"]) 
        if commit:
            app_setting.save()
        return app_setting