from django.contrib import admin
from django.urls import path
from core.create_customre.views import *
from core.user_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', users_list, name='user_list'),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout-user/', log_out_user, name='log_out_user'),
    path('sign-up/', sign_up, name='sign_up'),
    path('user-api/', user_api, name='user_api'),
    path('user-api/<int:user_id>/', single_user_api, name='single_user_api'),
    path('user-api-permission-name/', user_api_permission_name, name='user_api_permission-name'),
    path('user-api-permission/', user_api_permission, name='user_api_permission'),
    path('delete-user/', delete_user_api, name='delete_user'),
    path('delete-permission/', delete_permission_name, name='delete_permission'),
    path('delete-user-permission/', delete_user_permission, name='delete_user_permission'),
    path('edit-user-permission/<int:user_permisson_id>/', edit_user_permission, name='edit_user_permission'),
    path('authenticate-user/', user_authenticate, name='authenticate_user')
]
