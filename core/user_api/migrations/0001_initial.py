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
            name='UserApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=999)),
                ('user_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('user_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('customre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserApiPermissionName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_api_permission_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserApiPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(blank=True, default=False, null=True)),
                ('write', models.BooleanField(blank=True, default=False, null=True)),
                ('edit', models.BooleanField(blank=True, default=False, null=True)),
                ('delete', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_api', to='user_api.userapi')),
                ('user_api_permission_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_api_permission_name', to='user_api.userapipermissionname')),
            ],
        ),
    ]
