from django.db import models
from django.contrib.auth.models import User

class UserApi(models.Model):
    customre = models.ForeignKey(User, on_delete=models.PROTECT, related_name='customre')

    user_email = models.EmailField()
    user_password = models.CharField(max_length=999)

    user_first_name = models.CharField(max_length=255, null=True, blank=True)
    user_last_name = models.CharField(max_length=255, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.user_email)
    


class UserApiPermissionName(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    permission_name = models.CharField(max_length=255)
    

    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.permission_name)
    

class UserApiPermission(models.Model):
    user_api_permission_name = models.ForeignKey(UserApiPermissionName, on_delete=models.CASCADE, related_name='user_api_permission_name')
    user_api = models.ForeignKey(UserApi, on_delete=models.CASCADE, related_name='user_api')
    read = models.BooleanField(default=False, null=True, blank=True)
    write = models.BooleanField(default=False, null=True, blank=True)
    edit = models.BooleanField(default=False, null=True, blank=True)
    delete = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_api_permission_name)

