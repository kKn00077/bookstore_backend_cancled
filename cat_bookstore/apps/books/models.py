from django.db import models
from django.conf import settings

class Books(models.Model):
    """
        책 정보 (카카오 도서검색 api 참고)
    """

    book_id = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=500, verbose_name="도서 제목")
    contents = models.TextField(verbose_name="도서 소개")
    isbn = models.CharField(max_length=25,
                            verbose_name="ISBN 코드",
                            help_text="ISBN10 또는 ISBN13 중 하나 이상 포함. 두 값이 모두 제공될 경우 공백으로 구분")
    detail_url = models.URLField(max_length=settings.URL_MAX_LEN, verbose_name="도서 상세 URL")
    
    publication_date = models.DateTimeField(
        verbose_name="도서 출판 일시",
        help_text="""ISO 8601 형식, [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].000+[tz]"""
    )
    
    authors = models.CharField(max_length=300,
                                verbose_name="도서 저자",
                                help_text="여러 명일 경우 ,으로 구분")
    publisher = models.CharField(max_length=100, verbose_name="도서 출판사")
    translators = models.CharField(max_length=300, 
                                    verbose_name="도서 번역가",
                                    help_text="여러 명일 경우 ,으로 구분")
    
    price = models.IntegerField(verbose_name="도서 정가")
    sale_price = models.IntegerField(verbose_name="도서 판매가")
    
    thumbnail = models.URLField(max_length=settings.URL_MAX_LEN, null=True, verbose_name="도서 표지 미리보기 URL")

    class Meta:
        ordering = ['-book_id']

        verbose_name = '도서 정보'
        verbose_name_plural = '도서 정보'

    def __str__(self):
        return f'{self.title} - ({self.authors})'
