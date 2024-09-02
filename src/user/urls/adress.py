from django.urls import path
from ..views.adress import add_adress, list_adress, edit_adress, delete_adress

app_name = 'adress'

urlpatterns = [
    path('add-adress/', add_adress, name='add_adress'),
    path('list-adress/', list_adress, name='list_adress'),
    path('edit-adress/<int:id>', edit_adress, name='edit_adress'),
    path('delete-adress/<int:id>', delete_adress, name='delete_adress'),
]
