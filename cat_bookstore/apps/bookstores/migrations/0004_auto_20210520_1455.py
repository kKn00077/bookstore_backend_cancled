# Generated by Django 3.2.1 on 2021-05-20 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_alter_file_file_group'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstores', '0003_alter_bookstore_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookstore', to=settings.AUTH_USER_MODEL, verbose_name='유저 계정 정보'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='img_file_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.filegroup', verbose_name='서점 이미지 묶음 파일 정보'),
        ),
        migrations.AlterField(
            model_name='bookstorecategory',
            name='bookstore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstores.bookstore', verbose_name='서점'),
        ),
        migrations.AlterField(
            model_name='subscribeinfo',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자 계정 정보'),
        ),
        migrations.AlterField(
            model_name='subscribeinfo',
            name='bookstore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstores.bookstore', verbose_name='서점 정보'),
        ),
        migrations.AlterField(
            model_name='userlikedbookstore',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='사용자 계정 정보'),
        ),
        migrations.AlterField(
            model_name='userlikedbookstore',
            name='bookstore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstores.bookstore', verbose_name='서점 정보'),
        ),
    ]
