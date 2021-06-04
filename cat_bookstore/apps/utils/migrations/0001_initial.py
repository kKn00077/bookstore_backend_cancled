# Generated by Django 3.2.1 on 2021-06-04 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('app_version_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=10, verbose_name='버전')),
                ('status', models.CharField(choices=[('NEWEST', '최신 버전'), ('UPDATE_REQUIRED', '업데이트 필수'), ('UPDATE_RECOMMENDED', '업데이트 권장')], default='NEWEST', max_length=30, verbose_name='버전 상태')),
            ],
            options={
                'verbose_name': '앱 버전 관리',
                'verbose_name_plural': '앱 버전 관리',
                'ordering': ['-app_version_id'],
            },
        ),
    ]
