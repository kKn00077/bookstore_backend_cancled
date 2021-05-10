# Generated by Django 3.2.1 on 2021-05-07 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('push', '0002_auto_20210507_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpushinfo',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 계정 정보'),
        ),
        migrations.AlterField(
            model_name='userpushinfo',
            name='registration_token',
            field=models.CharField(max_length=500, primary_key=True, serialize=False, verbose_name='파이어베이스 토큰'),
        ),
    ]