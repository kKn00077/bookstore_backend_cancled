from django.db import models
from accounts.models import UserAccount
from model_utils.fields import AutoCreatedField

class UserPushInfo(models.Model):
    
    account_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    registration_token = models.CharField(max_length=500, primary_key=True)
    created = AutoCreatedField()

    class Meta:
        ordering = ['-account_id']

        verbose_name = '유저 푸시 정보'
        verbose_name_plural = '유저 푸시 정보'

    def __str__(self):
        return f'{self.registration_token}'