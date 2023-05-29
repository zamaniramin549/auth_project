# Generated by Django 4.2.1 on 2023-05-29 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_api', '0002_alter_userapipermission_user_api_permission_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapi',
            name='customre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customre', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userapipermission',
            name='user_api_permission_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_api_permission_name', to='user_api.userapipermissionname'),
        ),
        migrations.AlterField(
            model_name='userapipermissionname',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]