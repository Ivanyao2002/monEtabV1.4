from django.urls import path, include
 

urlpatterns = [
    path('', include('user.routers.user_urls')),
    path('role-user', include('user.routers.role_user_urls')),
]
