# Generated by Django 3.2.1 on 2021-06-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='이메일'),
        ),
    ]
