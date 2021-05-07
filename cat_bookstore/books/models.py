from django.db import models

class BooksInfo(models.Model):
    """
        크롤링 한 도서 정보 관련
    """

    book_id = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=500)
    contents = models.TextField()
    isbn = models.CharField(max_length=25, help_text="ISBN10 또는 ISBN13 중 하나 이상 포함. 두 값이 모두 제공될 경우 공백으로 구분")
    detail_url = models.URLField(max_length=500)
    
    publication_date = models.DateTimeField(\
        help_text="""ISO 8601 형식, [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].000+[tz]"""
    )
    
    authors = models.CharField(max_length=300, help_text="여러 명일 경우 ,으로 구분")
    publisher = models.CharField(max_length=100)
    translators = models.CharField(max_length=300, help_text="여러 명일 경우 ,으로 구분")
    
    price = models.IntegerField()
    sale_price = models.IntegerField()
    
    thumbnail = models.URLField(max_length=500, null=True)

    class Meta:
        ordering = ['-book_id']

        verbose_name = '도서 정보'
        verbose_name_plural = '도서 정보'

    def __str__(self):
        return f'{self.title} - ({self.authors})'