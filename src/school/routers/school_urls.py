from django.urls import path
from ..views.school_views import add_school, list_school, edit_school, delete_school, check_school

app_name = 'school'

urlpatterns = [
    path('', check_school, name='check_school'),
    path('add-school/', add_school, name='add_school'),
    path('list-school/', list_school, name='list_school'),
    path('edit-school/', edit_school, name='edit_school'),
    # path('delete-school/<int:id>', delete_school, name='delete_school'),
]
