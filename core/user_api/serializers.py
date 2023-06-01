from rest_framework import serializers
from .models import UserApi, UserApiPermission, UserApiPermissionName



        
class UserApiPermissionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApiPermissionName
        exclude = ['user']


class UserAPIPermissionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user_api')
    user_id = serializers.IntegerField(source='user_api.id')
    permission_name = serializers.CharField(source='user_api_permission_name')
    permission_name_id = serializers.IntegerField(source='user_api_permission_name.id')
    user_permission_id = serializers.IntegerField(source='id')
    class Meta:
        model = UserApiPermission
        exclude = ['customre', 'created', 'updated_at', 'id', 'user_api_permission_name', 'user_api']



class UserApiSerializer(serializers.ModelSerializer):
    permissions = UserAPIPermissionSerializer(many = True, source='user_api')
    class Meta:
        model = UserApi
        exclude = ['customre', 'created', 'updated_at', 'user_password']

