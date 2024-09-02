from django.urls import path
from ..views.teacher import add_teacher, list_teacher, edit_teacher, delete_teacher

app_name = 'teacher'

urlpatterns = [
    path('add-teacher/', add_teacher, name='add_teacher'),
    path('list-teacher/', list_teacher, name='list_teacher'),
    path('edit-teacher/<int:id>', edit_teacher, name='edit_teacher'),
    path('delete-teacher/<int:id>', delete_teacher, name='delete_teacher'),
]
