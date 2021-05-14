# Generated by Django 3.2.1 on 2021-05-10 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0004_auto_20210507_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookstore',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('bookstore_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='서점명')),
                ('address', models.CharField(max_length=100, verbose_name='서점 주소')),
                ('address_detail', models.CharField(max_length=100, verbose_name='서점 상세 주소')),
                ('introduction', models.TextField(blank=True, verbose_name='서점 소개')),
                ('is_affiliate', models.BooleanField(default=False, verbose_name='가맹점 여부')),
                ('account', models.ForeignKey(db_column='account_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='사장님 계정 정보')),
                ('img_file_group', models.ForeignKey(db_column='img_file_group_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.filegroup', verbose_name='서점 이미지 묶음 파일 정보')),
            ],
            options={
                'verbose_name': '서점 정보',
                'verbose_name_plural': '서점 정보',
                'ordering': ['-bookstore_id'],
            },
        ),
        migrations.CreateModel(
            name='UserLikedBookstore',
            fields=[
                ('liked_id', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.ForeignKey(db_column='account_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='사용자 계정 정보')),
                ('bookstore', models.ForeignKey(db_column='bookstore_id', on_delete=django.db.models.deletion.CASCADE, to='bookstores.bookstore', verbose_name='서점 정보')),
            ],
            options={
                'verbose_name': '사용자 좋아요 현황',
                'verbose_name_plural': '사용자 좋아요 현황',
                'ordering': ['-liked_id'],
                'unique_together': {('account', 'bookstore')},
            },
        ),
        migrations.CreateModel(
            name='SubscribeInfo',
            fields=[
                ('subscribe_id', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.ForeignKey(db_column='account_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자 계정 정보')),
                ('bookstore', models.ForeignKey(db_column='bookstore_id', on_delete=django.db.models.deletion.CASCADE, to='bookstores.bookstore', verbose_name='서점 정보')),
            ],
            options={
                'verbose_name': '사용자 구독 정보',
                'verbose_name_plural': '사용자 구독 정보',
                'ordering': ['-subscribe_id'],
                'unique_together': {('account', 'bookstore')},
            },
        ),
    ]