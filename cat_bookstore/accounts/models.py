from django.db import models
from files.models import File 
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
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
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

    STATUS = Choices('USE', 'DELETED', 'DORMANT')

    account_id = models.AutoField(primary_key=True)

    # 관리자 페이지 접근 권한
    is_staff = models.BooleanField(default=False)

    email = models.EmailField(max_length=255, unique=True, null=True)
    phone = models.CharField(max_length=11, unique=True)

    status = StatusField(max_length=30, default=STATUS.USE)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['-account_id']

        verbose_name = '유저 계정 정보'
        verbose_name_plural = '유저 계정 정보'

    def __str__(self):
        return f'{self.phone} ({self.email})'


class UserProfile(models.Model):
    """
        유저 프로필 정보
    """

    GENDER = Choices('MALE', 'FEMALE', 'OTHER')

    profile_id = models.AutoField(primary_key=True)

    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="account_id"
    )

    cat_img_file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL, db_column="cat_img_file_id", related_name="cat_img_file")
    cat_sound_file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL, db_column="cat_sound_file_id", related_name="cat_sound_file")
    profile_img_file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL, db_column="profile_img_file_id", related_name="profile_img_file")

    name = models.CharField(max_length=30)
    birth = models.DateField()
    nickname = models.CharField(max_length=30)
    gender = StatusField(max_length=30, choices_name='GENDER')

    class Meta:
        ordering = ['-profile_id']

        verbose_name = '일반 유저 프로필 정보'
        verbose_name_plural = '일반 유저 프로필 정보'

    def __str__(self):
        return f'{self.nickname} - {self.account}'


# TODO: 사장님 프로필 정보 필드 기획 후 재구성 필요함.
class OwnerUserProfile(models.Model):
    """
        사장님 프로필 정보
    """

    GENDER = Choices('MALE', 'FEMALE', 'OTHER')

    profile_id = models.AutoField(primary_key=True)

    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="account_id"
    )

    cat_img_file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL, db_column="cat_img_file_id", related_name="owner_cat_img_file")
    cat_sound_file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL, db_column="cat_sound_file_id", related_name="owner_cat_sound_file")
    profile_img_file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL, db_column="profile_img_file_id", related_name="owner_profile_img_file")
    
    name = models.CharField(max_length=30)
    birth = models.DateField()
    nickname = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=GENDER)

    class Meta:
        ordering = ['-profile_id']

        verbose_name = '사장님 프로필 정보'
        verbose_name_plural = '사장님 프로필 정보'

    def __str__(self):
        return f'{self.nickname} - {self.account}'


class UserCertification(models.Model):
    """
        유저 인증 정보
    """

    MAX_EMAIL_CODE_LEN = 6
    MAX_SMS_CODE_LEN = 6

    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column="account_id"
    )

    is_sms_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    
    sms_code = models.CharField(max_length=MAX_SMS_CODE_LEN, null=True)
    email_code = models.CharField(max_length=MAX_EMAIL_CODE_LEN, null=True)
    
    sms_time_limit = models.DateTimeField(null=True)
    email_time_limit = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-account']

        verbose_name = '유저 인증 정보'
        verbose_name_plural = '유저 인증 정보'

    def __str__(self):
        return f'{self.account}'