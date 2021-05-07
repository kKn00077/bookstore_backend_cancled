from django.db import models
from model_utils.models import TimeStampedModel

class AppNotice(TimeStampedModel):
    """
        앱 내 공지사항 관련
    """

    notice_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    contents = models.TextField()

    class Meta:
        ordering = ['-notice_id']

        verbose_name = '공지'
        verbose_name_plural = '공지'

    def __str__(self):
        return f'{self.title} ({self.created})'