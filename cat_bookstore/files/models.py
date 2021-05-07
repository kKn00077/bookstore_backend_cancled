from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings


class FileGroup(TimeStampedModel):
    """
        묶음 파일 관련 정보
    """

    file_group_id = models.AutoField(primary_key=True)
    class Meta:
        ordering = ['-created']

        verbose_name = '파일 그룹'
        verbose_name_plural = '파일 그룹'


class File(TimeStampedModel):
    """
        파일 업로드 관련 정보
    """

    file_id = models.AutoField(primary_key=True)

    file_group = models.ForeignKey(FileGroup, null=True, 
                                    on_delete=models.SET_NULL,
                                    verbose_name="파일 그룹",
                                    db_column="file_group_id")
    
    name = models.CharField(max_length=settings.URL_MAX_LEN, verbose_name="저장된 파일명")
    origin_name = models.CharField(max_length=settings.URL_MAX_LEN, verbose_name="원본 파일명")
    
    # TODO: upload 경로는 추후에 필요 시에 변경
    path = models.FileField(upload_to='img', max_length=settings.URL_MAX_LEN, verbose_name="저장된 파일 경로 (파일 업로드)")
    
    origin_path = models.CharField(max_length=settings.URL_MAX_LEN, verbose_name="원본 파일 경로")
    
    file_type = models.CharField(max_length=30, verbose_name="파일 확장자")
    
    size = models.IntegerField(verbose_name="파일 크기")
    
    order = models.IntegerField(default=1, null=True, verbose_name="파일 정렬 순", help_text="묶음 파일일 경우 적용됩니다.")

    class Meta:
        ordering = ['-created']

        verbose_name = '파일'
        verbose_name_plural = '파일'

    def __str__(self):
        return f'{self.name} ({self.path})'
