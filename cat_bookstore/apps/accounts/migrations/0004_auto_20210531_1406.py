# Generated by Django 3.2.1 on 2021-05-31 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_useraccount_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercertification',
            name='certification_id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usercertification',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certification', to=settings.AUTH_USER_MODEL, verbose_name='유저 계정 정보'),
        ),
    ]