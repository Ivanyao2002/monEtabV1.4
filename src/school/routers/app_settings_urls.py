from django.urls import path
from ..views.app_settings_views import add_setting, list_setting, edit_setting, delete_setting, check_settings
 
app_name = 'setting'

urlpatterns = [
    path('', check_settings, name= 'check_settings'),
    path('add-setting/', add_setting, name='add_setting'),
    path('list-setting/', list_setting, name='list_setting'),
    path('edit-setting/<int:id>', edit_setting, name='edit_setting'),
    path('delete-setting/<int:id>', delete_setting, name='delete_setting'),
]
