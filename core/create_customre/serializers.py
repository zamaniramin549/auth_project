from django.contrib.auth.models import User
from rest_framework import serializers
from .models import APIAccess


class APIAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIAccess
        exclude = ['id', 'user']


class UserSerializer(serializers.ModelSerializer):
    api = APIAccessSerializer(many = True)
    class Meta:
        model = User
        exclude = ['id', 'password', 'is_staff', 'is_active', 'groups', 'user_permissions', 'is_superuser']