# Generated by Django 3.2.1 on 2021-05-07 06:28

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpushinfo',
            name='modified',
        ),
        migrations.AlterField(
            model_name='userpushinfo',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False),
        ),
    ]