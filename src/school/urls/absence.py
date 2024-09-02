from django.urls import path
from ..views.absence import add_absence, list_absence, edit_absence, delete_absence

app_name = 'absence'

urlpatterns = [
    path('add-absence/', add_absence, name='add_absence'),
    path('list-absence/', list_absence, name='list_absence'),
    path('edit-absence/<int:id>', edit_absence, name='edit_absence'),
    path('delete-absence/<int:id>', delete_absence, name='delete_absence'),
]
