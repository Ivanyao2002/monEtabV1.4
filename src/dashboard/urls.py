from django.urls import path
from .views import index

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', index, name='index'),
]
