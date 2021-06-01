# Generated by Django 3.2.1 on 2021-06-01 02:42

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppNotice',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300, verbose_name='공지 제목')),
                ('contents', models.TextField(verbose_name='공지 내용')),
            ],
            options={
                'verbose_name': '공지',
                'verbose_name_plural': '공지',
                'ordering': ['-notice_id'],
            },
        ),
    ]
