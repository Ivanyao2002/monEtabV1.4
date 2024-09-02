from django.urls import path
from .views import add_setting, list_setting, edit_setting, delete_setting
 
app_name = 'setting'

urlpatterns = [
    path('add-setting/', add_setting, name='add_setting'),
    path('list-setting/', list_setting, name='list_setting'),
    path('edit-setting/<int:id>', edit_setting, name='edit_setting'),
    path('delete-setting/<int:id>', delete_setting, name='delete_setting'),
]
