from django.db import models


class UserStatusChoice(models.TextChoices):
    USE = "USE", "사용"
    DELETED = "DELETED", "탈퇴"
    DORMANT = "DORMANT", "휴면"


class CertificationTypeChoice(models.TextChoices):
    EMAIL = "EMAIL", "이메일"
    SMS = "SMS", "핸드폰"