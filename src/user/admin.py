from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
from .models.role_user_model import RoleUserModel
from .models.user_model import UserModel


# Register your models here.
admin.site.register(RoleUserModel)
@admin.register(UserModel)
class AdminUser(UserAdmin):
    pass
