from django.db import models
from django.contrib.auth.models import User



class APIAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api')
    test_api = models.CharField(max_length=255)
    production_api = models.CharField(max_length=255)
    uuid = models.UUIDField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

