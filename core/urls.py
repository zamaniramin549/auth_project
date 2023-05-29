from django.contrib import admin
from django.urls import path
from core.create_customre.views import *
from core.user_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_list, name='user_list'),
    path('user-api/', user_api, name='user_api'),
    path('user-api-permission-name/', user_api_permission_name, name='user_api_permission-name'),
    path('user-api-permission/', user_api_permission, name='user_api_permission')
]
