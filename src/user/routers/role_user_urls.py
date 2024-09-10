from django.urls import path
from ..views.role_user_views import add_role_user, list_role_user, edit_role_user, delete_role_user

app_name = 'role_user'

urlpatterns = [
    path('add-role-user/', add_role_user, name='add_role_user'),
    path('list-role-user/', list_role_user, name='list_role_user'),
    path('edit-role-user/<str:role>', edit_role_user, name='edit_role_user'),
    path('delete-role-user/<str:role>', delete_role_user, name='delete_role_user'),
]
