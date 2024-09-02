from django.urls import path
from ..views.school import add_school, list_school, edit_school, delete_school

app_name = 'school'

urlpatterns = [
    path('add-school/', add_school, name='add_school'),
    path('list-school/', list_school, name='list_school'),
    path('edit-school/<int:id>', edit_school, name='edit_school'),
    path('delete-school/<int:id>', delete_school, name='delete_school'),
]