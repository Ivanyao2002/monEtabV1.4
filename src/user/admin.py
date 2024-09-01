from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
from .models.adress import AdressModel
from .models.role_user import RoleUserModel
from .models.user import UserModel


# Register your models here.
admin.site.register(AdressModel)
admin.site.register(RoleUserModel)
@admin.register(UserModel)
class AdminUser(UserAdmin):
    pass
