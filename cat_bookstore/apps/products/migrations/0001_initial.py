# Generated by Django 3.2.1 on 2021-06-01 02:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookstores', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='상품 명')),
                ('contents', models.TextField(verbose_name='상품 설명')),
                ('price', models.IntegerField(verbose_name='상품 가격')),
                ('product_type', models.CharField(max_length=30, verbose_name='상품 타입')),
                ('bookstore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstores.bookstore', verbose_name='서점')),
            ],
            options={
                'verbose_name': '서점 별 상품관리',
                'verbose_name_plural': '서점 별 상품관리',
                'ordering': ['-product_id'],
            },
        ),
        migrations.CreateModel(
            name='BookStock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0, verbose_name='수량')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='추천도서 여부')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books', verbose_name='책')),
                ('bookstore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstores.bookstore', verbose_name='서점')),
            ],
            options={
                'verbose_name': '서점 별 책 재고',
                'verbose_name_plural': '서점 별 책 재고',
                'ordering': ['-stock_id'],
            },
        ),
    ]
