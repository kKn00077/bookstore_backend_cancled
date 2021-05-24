from django.db import models


class UserStatusChoice(models.TextChoices):
    USE = "USE", "사용"
    DELETED = "DELETED", "탈퇴"
    DORMANT = "DORMANT", "휴면"
