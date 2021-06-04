from django.db import models
from .enums import VersionStatusChoice

class AppVersion(models.Model):
    """
    앱 버전 관리
    """

    app_version_id = models.AutoField(primary_key=True)

    version = models.CharField(
        "버전", max_length=10
    )

    status = models.CharField(
        "버전 상태", max_length=30,
        choices=VersionStatusChoice.choices,
        default=VersionStatusChoice.NEWEST
    )

    class Meta:
        ordering = ["-app_version_id"]

        verbose_name = "앱 버전 관리"
        verbose_name_plural = "앱 버전 관리"

    def __str__(self):
        return f"{self.version} - {self.get_status_display()}"
