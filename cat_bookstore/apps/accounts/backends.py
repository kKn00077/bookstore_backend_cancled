from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model
from apps.profiles.models import OwnerUserProfile

UserAccount = get_user_model()

class AuthBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return UserAccount.objects.get(pk=user_id)
        except UserAccount.DoesNotExist:
            return None


    def authenticate(self, request, username=None, password=None, **kwargs):
        """
            커스텀 인증

            인증된 사용자를 받아오기 위해
            email, phone, password를 선택적으로 인자로 받아서
            해당 정보를 바탕으로 유저 정보를 가져옴
        """

        is_crm = kwargs.get('is_crm', False)
        
        try:
            # phone 정보가 있으면 phone을 통해 유저 정보를 가져옴
            if username is not None:
                user = UserAccount.objects.get(~Q(status='DELETED'), phone=username)
            # phone 정보가 없을 경우 email을 통해 유저 정보를 가져옴
            else:
                user = UserAccount.objects.get(~Q(status='DELETED'), email=kwargs['email'])

            # CRM 로그인일 경우 사장님인지 아닌지 체크
            if is_crm:
                user.owner_profile

        except (UserAccount.DoesNotExist, OwnerUserProfile.DoesNotExist):
            return None

        # 받아온 password와 위에서 조회한 유저의 password가 일치하면
        # user 정보 반환, 아닐 경우 None 반환
        return user if user.check_password(password) else None