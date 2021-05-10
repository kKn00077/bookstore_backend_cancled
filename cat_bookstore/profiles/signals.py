from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserAccount

@receiver(post_save, sender=UserAccount)
def save_user_profile(sender, instance, **kwargs):
    # TODO: 유저 프로필 정보 인스턴스 save 코드 작성
    # TODO: 일반유저/사장님유저 구분

    pass