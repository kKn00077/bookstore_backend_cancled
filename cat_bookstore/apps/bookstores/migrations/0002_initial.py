# Generated by Django 3.2.1 on 2021-06-01 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookstores', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
        ('books', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='account',
            field=models.ManyToManyField(related_name='subscribe_category', through='profiles.CategorySubscribe', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='bookstore',
            field=models.ManyToManyField(related_name='category', through='bookstores.BookstoreCategory', to='bookstores.Bookstore'),
        ),
        migrations.AddField(
            model_name='bookstorecategory',
            name='bookstore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstores.bookstore', verbose_name='서점'),
        ),
        migrations.AddField(
            model_name='bookstorecategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookstores.category', verbose_name='카테고리'),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookstore', to=settings.AUTH_USER_MODEL, verbose_name='유저 계정 정보'),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='book_stock',
            field=models.ManyToManyField(related_name='bookstore', through='products.BookStock', to='books.Books'),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='img_file_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.filegroup', verbose_name='서점 이미지 묶음 파일 정보'),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked', through='bookstores.UserLikedBookstore', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='subscribed_users',
            field=models.ManyToManyField(related_name='subscribed', through='bookstores.SubscribeInfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userlikedbookstore',
            unique_together={('account', 'bookstore')},
        ),
        migrations.AlterUniqueTogether(
            name='subscribeinfo',
            unique_together={('account', 'bookstore')},
        ),
    ]
