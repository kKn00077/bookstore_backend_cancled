from django.db import models
from model_utils.models import TimeStampedModel


class BookStock(models.Model):
    """
        서점 별 책 재고
    """

    stock_id = models.AutoField(primary_key=True)

    bookstore = models.ForeignKey(
        "bookstores.Bookstore",
        verbose_name="서점",
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        "books.Books",
        verbose_name="책",
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField("수량", default=0)
    is_recommend = models.BooleanField("추천도서 여부", default=False)

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
        verbose_name="서점",
        on_delete=models.CASCADE,
    )

    name = models.CharField("상품 명", max_length=100)
    contents = models.TextField("상품 설명")
    price = models.IntegerField("상품 가격")
    product_type = models.CharField("상품 타입", max_length=30)

    class Meta:
        ordering = ['-product_id']

        verbose_name = '서점 별 상품관리'
        verbose_name_plural = '서점 별 상품관리'

    def __str__(self):
        return f'{self.bookstore} - ({self.name})'