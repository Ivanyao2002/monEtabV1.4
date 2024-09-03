from django.contrib import admin
from .models.school_model import SchoolModel
from .models.app_settings_model import AppSettingModel


# Register your models here.
admin.site.register(SchoolModel)
admin.site.register(AppSettingModel)