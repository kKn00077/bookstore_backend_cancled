from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings


class FileGroup(TimeStampedModel):
    file_group_id = models.AutoField(primary_key=True)
    class Meta:
        ordering = ['-created']

        verbose_name = '파일 그룹'
        verbose_name_plural = '파일 그룹'


class File(TimeStampedModel):

    FILE_URL_MAX_LEN = 260

    file_id = models.AutoField(primary_key=True)

    file_group = models.ForeignKey(FileGroup, null=True, on_delete=models.SET_NULL, db_column="file_group_id")
    
    name = models.CharField(max_length=FILE_URL_MAX_LEN)
    origin_name = models.CharField(max_length=FILE_URL_MAX_LEN)
    
    # TODO: upload 경로는 추후에 필요 시에 변경
    path = models.FileField(upload_to='img')
    
    origin_path = models.CharField(max_length=FILE_URL_MAX_LEN)
    
    file_type = models.CharField(max_length=30)
    
    size = models.IntegerField()
    
    order = models.IntegerField(default=1, null=True)

    class Meta:
        ordering = ['-created']

        verbose_name = '파일'
        verbose_name_plural = '파일'

    def __str__(self):
        return f'{self.name} ({self.path})'
