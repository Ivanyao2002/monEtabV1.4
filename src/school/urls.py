from django.urls import path
from .views.teacher import add_teacher, list_teacher

app_name = 'school'

urlpatterns = [
    path('', add_teacher, name='add_teacher'),
    path('list/', list_teacher, name='list_teacher'),
]
