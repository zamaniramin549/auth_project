from django.db import models
from django.contrib.auth.models import User
import uuid

test_api_uuid = 'test_api_' + str(uuid.uuid4())
production_api_uuid = 'live_api_' + str(uuid.uuid4())

class APIAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api')
    test_api = models.CharField(max_length=255, default=test_api_uuid)
    production_api = models.CharField(max_length=255, default=production_api_uuid)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

