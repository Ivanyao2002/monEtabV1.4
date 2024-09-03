from django.urls import path
from ..views.student_views import add_student, list_student, edit_student, delete_student

app_name = 'student'

urlpatterns = [
    path('add-student/', add_student, name='add_student'),
    path('list-student/', list_student, name='list_student'),
    path('edit-student/<int:id>', edit_student, name='edit_student'),
    path('delete-student/<int:id>', delete_student, name='delete_student'),
]
