from django.urls import path, include
 

urlpatterns = [
    path('', include('school.routers.school_urls')),
    path('setting/', include('school.routers.app_settings_urls')),
]
