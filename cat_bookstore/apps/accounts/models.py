from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from model_utils import Choices
from model_utils.fields import StatusField
from django.conf import settings


class UserManager(BaseUserManager):
    """
        User를 생성할때 사용하는 클래스
    """

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """
        Creates and saves a User with the given phone and password.
        """

        if not phone:
            raise ValueError('The given phone must be set')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """
            일반 유저 생성 시
        """

        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """
            superuser 생성 시
            
            어드민 페이지 접근 권한(is_staff) True 설정
            슈퍼유저 권한(is_superuser) True 설정
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)

class UserAccount(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    """
        유저의 계정정보
    """

    objects = UserManager()

    # 계정 상태 값 ('USE' - 사용, 'DELETED' - 탈퇴, 'DORMANT' - 휴면)
    STATUS = Choices('USE', 'DELETED', 'DORMANT')

    account_id = models.AutoField(primary_key=True)

    # 관리자 페이지 접근 권한
    is_staff = models.BooleanField(default=False, verbose_name="관리자 페이지 접근 권한")

    email = models.EmailField(max_length=255, unique=True, null=True, verbose_name="이메일")
    phone = models.CharField(max_length=11, unique=True, verbose_name="휴대폰 번호")

    status = StatusField(max_length=30, default=STATUS.USE,
                        verbose_name="계정 상태",
                        help_text="USE - 사용 / DELETED - 탈퇴 / DORMANT - 휴면")

    # 이메일 필드
    EMAIL_FIELD = 'email'

    # 계정 ID로 사용할 필드
    USERNAME_FIELD = 'phone'
    
    # ID, PW 이외의 필수로 받아야 하는 필드
    # REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['-account_id']

        verbose_name = '유저 계정 정보'
        verbose_name_plural = '유저 계정 정보'

    def __str__(self):
        return f'{self.phone} ({self.email})'


class UserCertification(models.Model):
    """
        유저 인증 정보
    """

    # 이메일 인증 코드 길이
    MAX_EMAIL_CODE_LEN = 6

    # SMS 인증 코드 길이
    MAX_SMS_CODE_LEN = 6

    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name="유저 계정 정보",
        db_column="account_id",
        related_name="certification"
    )

    is_sms_verified = models.BooleanField(default=False, verbose_name="SMS 인증 여부")
    is_email_verified = models.BooleanField(default=False, verbose_name="이메일 인증 여부")
    
    sms_code = models.CharField(max_length=MAX_SMS_CODE_LEN, null=True, verbose_name="SMS 인증 코드")
    email_code = models.CharField(max_length=MAX_EMAIL_CODE_LEN, null=True, verbose_name="이메일 인증 코드")
    
    sms_time_limit = models.DateTimeField(null=True, verbose_name="SMS 인증 제한 일시")
    email_time_limit = models.DateTimeField(null=True, verbose_name="이메일 인증 제한 일시")

    class Meta:
        ordering = ['-account']

        verbose_name = '유저 인증 정보'
        verbose_name_plural = '유저 인증 정보'

    def __str__(self):
        return f'{self.account}'