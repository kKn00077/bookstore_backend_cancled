from django.db import models
from accounts.models import UserAccount
from model_utils.fields import AutoCreatedField

class UserPushInfo(models.Model):
    """
        유저 푸시 정보 관련
    """
    
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="유저 계정 정보")

    registration_token = models.CharField(max_length=500, primary_key=True, verbose_name="파이어베이스 토큰")
    created = AutoCreatedField()

    class Meta:
        ordering = ['-account_id']

        verbose_name = '유저 푸시 정보'
        verbose_name_plural = '유저 푸시 정보'

    def __str__(self):
        return f'{self.registration_token}'