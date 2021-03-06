from django.db import models
from model_utils.fields import AutoCreatedField
from django.contrib.auth import get_user_model

UserAccount = get_user_model()

class UserPushInfo(models.Model):
    """
    유저 푸시 정보 관련
    """

    account = models.ForeignKey(
        UserAccount, verbose_name="유저 계정 정보", on_delete=models.CASCADE
    )

    registration_token = models.CharField(
        max_length=500, verbose_name="파이어베이스 토큰", primary_key=True
    )
    created = AutoCreatedField()

    class Meta:
        ordering = ["-account_id"]

        verbose_name = "유저 푸시 정보"
        verbose_name_plural = "유저 푸시 정보"

    def __str__(self):
        return f"{self.registration_token}"
