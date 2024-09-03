from django.urls import path
from ..views.user_views import sign_in, register, log_out, add_user, edit_user, list_user, delete_user

app_name = 'user'

urlpatterns = [
    path('login/', sign_in, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
    path('add-user/', add_user, name='add_user'),
    path('list-user/', list_user, name='list_user'),
    path('edit-user/<int:id>', edit_user, name='edit_user'),
    path('delete-user/<int:id>', delete_user, name='delete_user'),
]
