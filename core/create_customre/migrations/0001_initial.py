# Generated by Django 4.2.1 on 2023-05-29 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APIAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_api', models.CharField(default='test_api_c8e994a9-b9be-417b-81ad-7e5b276ac5bb', max_length=255)),
                ('production_api', models.CharField(default='live_api_5682abf4-a75d-423d-9b13-2c4652332cc1', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]