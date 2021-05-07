# Generated by Django 3.2.1 on 2021-05-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksinfo',
            name='authors',
            field=models.CharField(help_text='여러 명일 경우 ,으로 구분', max_length=300, verbose_name='도서 저자'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='contents',
            field=models.TextField(verbose_name='도서 소개'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='detail_url',
            field=models.URLField(max_length=500, verbose_name='도서 상세 URL'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='isbn',
            field=models.CharField(help_text='ISBN10 또는 ISBN13 중 하나 이상 포함. 두 값이 모두 제공될 경우 공백으로 구분', max_length=25, verbose_name='ISBN 코드'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='price',
            field=models.IntegerField(verbose_name='도서 정가'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='publication_date',
            field=models.DateTimeField(help_text='ISO 8601 형식, [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].000+[tz]', verbose_name='도서 출판 일시'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='publisher',
            field=models.CharField(max_length=100, verbose_name='도서 출판사'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='sale_price',
            field=models.IntegerField(verbose_name='도서 판매가'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='thumbnail',
            field=models.URLField(max_length=500, null=True, verbose_name='도서 표지 미리보기 URL'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='title',
            field=models.CharField(max_length=500, verbose_name='도서 제목'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='translators',
            field=models.CharField(help_text='여러 명일 경우 ,으로 구분', max_length=300, verbose_name='도서 번역가'),
        ),
    ]
