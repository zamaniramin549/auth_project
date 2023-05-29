from rest_framework import serializers
from .models import UserApi, UserApiPermission, UserApiPermissionName



        
class UserApiPermissionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApiPermissionName
        exclude = ['user']


class UserAPIPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApiPermission
        fields = '__all__'



class UserApiSerializer(serializers.ModelSerializer):
    user_api = UserAPIPermissionSerializer(many = True)
    class Meta:
        model = UserApi
        exclude = ['customre', 'created', 'updated_at']

