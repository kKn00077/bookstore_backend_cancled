from django.db import models
from model_utils.models import TimeStampedModel


class BookStock(models.Model):
    """
        서점 별 책 재고
    """

    stock_id = models.AutoField(primary_key=True)

    bookstore = models.ForeignKey(
        "bookstores.Bookstore",
        on_delete=models.CASCADE,
        verbose_name="서점",
        db_column="bookstore_id",
    )
    book = models.ForeignKey(
        "books.Books",
        on_delete=models.CASCADE,
        verbose_name="책",
        db_column="book_id",
    )

    quantity = models.IntegerField(default=0, verbose_name="수량")
    is_recommend = models.BooleanField(default=False, verbose_name="추천도서 여부")

    class Meta:
        ordering = ['-stock_id']

        verbose_name = '서점 별 책 재고'
        verbose_name_plural = '서점 별 책 재고'

    def __str__(self):
        return f'{self.bookstore} - ({self.book})'


class Product(TimeStampedModel):
    product_id = models.AutoField(primary_key=True)

    bookstore = models.ForeignKey(
        "bookstores.Bookstore",
        on_delete=models.CASCADE,
        verbose_name="서점",
        db_column="bookstore_id",
    )

    name = models.CharField(max_length=100, verbose_name="상품 명")
    contents = models.TextField(verbose_name="상품 설명")
    price = models.IntegerField(verbose_name="상품 가격")
    product_type = models.CharField(max_length=30, verbose_name="상품 타입")

    class Meta:
        ordering = ['-product_id']

        verbose_name = '서점 별 상품관리'
        verbose_name_plural = '서점 별 상품관리'

    def __str__(self):
        return f'{self.bookstore} - ({self.name})'