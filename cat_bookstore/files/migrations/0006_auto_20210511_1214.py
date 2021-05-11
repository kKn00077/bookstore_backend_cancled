# Generated by Django 3.2.1 on 2021-05-11 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_alter_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.CharField(editable=False, max_length=30, verbose_name='파일 확장자'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(editable=False, max_length=500, verbose_name='저장된 파일명'),
        ),
        migrations.AlterField(
            model_name='file',
            name='origin_name',
            field=models.CharField(editable=False, max_length=500, verbose_name='원본 파일명'),
        ),
        migrations.AlterField(
            model_name='file',
            name='origin_path',
            field=models.CharField(editable=False, max_length=500, verbose_name='원본 파일 경로'),
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.IntegerField(editable=False, verbose_name='파일 크기'),
        ),
    ]
