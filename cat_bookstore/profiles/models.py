from django.db import models
from files.models import File 
from model_utils import Choices
from model_utils.fields import StatusField
from django.conf import settings


class UserProfile(models.Model):
    """
        유저 프로필 정보
    """

    GENDER = Choices('MALE', 'FEMALE', 'OTHER')

    profile_id = models.AutoField(primary_key=True)

    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="account_id",
        related_name="profile"
    )

    cat_img_file = models.ForeignKey(File, null=True, 
                                    on_delete=models.SET_NULL,
                                    db_column="cat_img_file_id", 
                                    related_name="cat_img_file",
                                    verbose_name="고양이 이미지 파일")
    cat_sound_file = models.ForeignKey(File, null=True, 
                                    on_delete=models.SET_NULL, 
                                    db_column="cat_sound_file_id", 
                                    related_name="cat_sound_file",
                                    verbose_name="고양이 사운드 파일")
    profile_img_file = models.ForeignKey(File, null=True, 
                                    on_delete=models.SET_NULL, 
                                    db_column="profile_img_file_id", 
                                    related_name="profile_img_file",
                                    verbose_name="프로필 이미지 파일")

    name = models.CharField(max_length=30, verbose_name="사용자 명")
    birth = models.DateField(verbose_name="사용자 생년월일")
    nickname = models.CharField(max_length=30, verbose_name="사용자 닉네임")
    gender = StatusField(max_length=30, choices_name='GENDER', verbose_name="사용자 성별")

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
        db_column="account_id",
        related_name="owner_profile"
    )

    cat_img_file = models.ForeignKey(File, null=True, 
                                    on_delete=models.SET_NULL,
                                    db_column="cat_img_file_id", 
                                    related_name="owner_cat_img_file",
                                    verbose_name="고양이 이미지 파일")
    cat_sound_file = models.ForeignKey(File, null=True, 
                                    on_delete=models.SET_NULL, 
                                    db_column="cat_sound_file_id", 
                                    related_name="owner_cat_sound_file",
                                    verbose_name="고양이 사운드 파일")
    profile_img_file = models.ForeignKey(File, null=True, 
                                    on_delete=models.SET_NULL, 
                                    db_column="profile_img_file_id", 
                                    related_name="owner_profile_img_file",
                                    verbose_name="프로필 이미지 파일")

    name = models.CharField(max_length=30, verbose_name="사용자 명")
    birth = models.DateField(verbose_name="사용자 생년월일")
    nickname = models.CharField(max_length=30, verbose_name="사용자 닉네임")
    gender = StatusField(max_length=30, choices_name='GENDER', verbose_name="사용자 성별")

    class Meta:
        ordering = ['-profile_id']

        verbose_name = '사장님 프로필 정보'
        verbose_name_plural = '사장님 프로필 정보'

    def __str__(self):
        return f'{self.nickname} - {self.account}'

