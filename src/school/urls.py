from django.urls import path, include
 

urlpatterns = [
    path('', include('school.routers.app_settings_urls')),
    path('school/', include('school.routers.school_urls')),
]
