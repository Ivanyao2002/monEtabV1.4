from django.urls import path, include
 

urlpatterns = [
    path('', include('student.routers.student_urls')),
    path('student-cards/', include('student.routers.student_cards_urls')),
    path('absence/', include('student.routers.absence_urls')),
]
