# Generated by Django 3.2.1 on 2021-05-06 08:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileGroup',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('file_group_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=260)),
                ('origin_name', models.CharField(max_length=260)),
                ('path', models.FileField(upload_to='img')),
                ('origin_path', models.CharField(max_length=260)),
                ('file_type', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('order', models.IntegerField(default=1, null=True)),
                ('file_group', models.ForeignKey(db_column='file_group_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.filegroup')),
            ],
            options={
                'verbose_name': '파일',
                'verbose_name_plural': '파일',
                'ordering': ['-created'],
            },
        ),
    ]
