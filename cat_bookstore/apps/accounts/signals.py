from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserAccount, UserCertification


@receiver(post_save, sender=UserAccount)
def save_user_certification(sender, instance, **kwargs):
    certification = UserCertification(account=instance)
    certification.save()
