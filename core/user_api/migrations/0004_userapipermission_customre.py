# Generated by Django 4.2.1 on 2023-05-29 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_api', '0003_alter_userapi_customre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapipermission',
            name='customre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='customre_user_api_permission', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
