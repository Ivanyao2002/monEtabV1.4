from django.urls import path, include
 

urlpatterns = [
    path('', include('base.routers.adress_urls')),
]
