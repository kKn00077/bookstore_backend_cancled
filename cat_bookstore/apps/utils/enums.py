from django.db import models

class VersionStatusChoice(models.TextChoices):
    # 현재 버전 엑세스를 허용함
    NEWEST = "NEWEST", "최신 버전"

    # 현재 버전 액세스를 허용하지 않음, 업데이트 필수
    UPDATE_REQUIRED = 'UPDATE_REQUIRED', "업데이트 필수"

    # 현재 버전 액세스를 허용함, 업데이트 권장
    UPDATE_RECOMMENDED = 'UPDATE_RECOMMENDED', "업데이트 권장"