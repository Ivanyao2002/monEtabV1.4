from django.urls import path, include
 

urlpatterns = [
    path('', include('teacher.routers.teacher_urls')),
]
