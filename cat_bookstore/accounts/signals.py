from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserAccount

@receiver(post_save, sender=UserAccount)
def create_user_certification(sender, instance, created, **kwargs):
    # TODO: 유저 인증 정보 인스턴스 생성 코드 작성
    pass
    
@receiver(post_save, sender=UserAccount)
def save_user_certification(sender, instance, **kwargs):
    # TODO: 유저 인증 정보 인스턴스 save 코드 작성
    pass