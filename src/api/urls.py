from django.urls import path
from .apiviews import student_api_views, teacher_api_view

urlpatterns = [
    path('', student_api_views.student_list),
    path('teacher/', teacher_api_view.teacher_list),
]