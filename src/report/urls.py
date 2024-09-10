from django.urls import path
from . import views 
 

app_name = 'report'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate-excel-student-list', views.students_list_to_excel, name='students_list_to_excel'),
    path('generate-excel-teacher-list', views.teachers_list_to_excel, name='teachers_list_to_excel'),
    path('generate-excel-user-list', views.users_list_to_excel, name='users_list_to_excel'),
    path('generate-pdf-student-list', views.students_list_to_pdf, name='students_list_to_pdf'),
    path('generate-pdf-teacher-list', views.teachers_list_to_pdf, name='teachers_list_to_pdf'),
    path('generate-pdf-user-list', views.users_list_to_pdf, name='users_list_to_pdf'),

]
