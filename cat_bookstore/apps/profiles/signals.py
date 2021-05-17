from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

UserAccount = get_user_model()


@receiver(post_save, sender=UserAccount)
def save_user_profile(sender, instance, created, **kwargs):

    # 비즈니스 코드 부분에서 먼저 인스턴스를 넣어주고
    # signals 에서 저장하는 방식
    profile = None

    # 유저가 아닐 경우 유저 프로필을 가져와 저장하려 하면
    # 에러가 나므로 에러가 발생 시 사장님으로 프로필을 저장
    if created:
        try:
            # 유저 프로필을 가져온다.
            profile = instance.profile
        except UserProfile.DoesNotExist:
            # 못가져올 경우 사장님 프로필을 가져온다.
            profile = instance.owner_profile
        finally:
            profile.save()
    
