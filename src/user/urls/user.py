from django.urls import path
from ..views.user import sign_in, register, log_out

app_name = 'user'

urlpatterns = [
    path('login/', sign_in, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
]
