from django.db import models


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
        return f'{self} - ({self.quantity})'
