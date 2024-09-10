from django.urls import path
from .apiviews import student_api_views, teacher_api_view

urlpatterns = [
    path('students/', student_api_views.student_list),
    path('teachers/', teacher_api_view.teacher_list),
]