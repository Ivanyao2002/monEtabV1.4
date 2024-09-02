from django.urls import path
from ..views.student_cards import add_student_card, list_student_card, edit_student_card, delete_student_card

app_name = 'student_cards'

urlpatterns = [
    path('add-student-card/', add_student_card, name='add_student_card'),
    path('list-student-card/', list_student_card, name='list_student_card'),
    path('edit-student-card/<int:id>', edit_student_card, name='edit_student_card'),
    path('delete-student-card/<int:id>', delete_student_card, name='delete_student_card'),
]
