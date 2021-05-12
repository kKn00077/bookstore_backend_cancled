from django.db import models
from model_utils.models import TimeStampedModel


class Bookstore(TimeStampedModel):
    """
    서점 정보 관련
    """

    bookstore_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(
        "accounts.UserAccount",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="사장님 계정 정보",
        db_column="account_id",
    )

    img_file_group = models.ForeignKey(
        "files.FileGroup",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="서점 이미지 묶음 파일 정보",
        db_column="img_file_group_id",
    )

    name = models.CharField(max_length=30, verbose_name="서점명")
    address = models.CharField(max_length=100, verbose_name="서점 주소")
    address_detail = models.CharField(max_length=100, verbose_name="서점 상세 주소")
    introduction = models.TextField(blank=True, verbose_name="서점 소개")

    is_affiliate = models.BooleanField(default=False, verbose_name="가맹점 여부")

    subscribed_users = models.ManyToManyField(
        "accounts.UserAccount", through="SubscribeInfo", related_name="subscribed"
    )
    liked_users = models.ManyToManyField(
        "accounts.UserAccount", through="UserLikedBookstore", related_name="liked"
    )

    class Meta:
        ordering = ["-bookstore_id"]

        verbose_name = "서점 정보"
        verbose_name_plural = "서점 정보"

    def __str__(self):
        return f"{self.name} - {self.address}"


class SubscribeInfo(models.Model):
    """
    사용자 구독 정보
    """

    subscribe_id = models.AutoField(primary_key=True)

    account = models.ForeignKey(
        "accounts.UserAccount",
        on_delete=models.CASCADE,
        verbose_name="사용자 계정 정보",
        db_column="account_id",
    )

    bookstore = models.ForeignKey(
        Bookstore,
        on_delete=models.CASCADE,
        verbose_name="서점 정보",
        db_column="bookstore_id",
    )

    class Meta:
        ordering = ["-subscribe_id"]

        verbose_name = "사용자 구독 정보"
        verbose_name_plural = "사용자 구독 정보"

        unique_together = (("account", "bookstore"),)

    def __str__(self):
        return f"{self.account} - {self.bookstore}"


class UserLikedBookstore(models.Model):
    """
    사용자 좋아요 현황
    """

    liked_id = models.AutoField(primary_key=True)

    # 좋아요를 누른 사용자가 탈퇴해도 서점의 좋아요는 그대로여야 하기 때문에
    # null값을 허용함
    account = models.ForeignKey(
        "accounts.UserAccount",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="사용자 계정 정보",
        db_column="account_id",
    )

    bookstore = models.ForeignKey(
        Bookstore,
        on_delete=models.CASCADE,
        verbose_name="서점 정보",
        db_column="bookstore_id",
    )

    class Meta:
        ordering = ["-liked_id"]

        verbose_name = "사용자 좋아요 현황"
        verbose_name_plural = "사용자 좋아요 현황"

        unique_together = (("account", "bookstore"),)

    def __str__(self):
        return f"{self.account} - {self.bookstore}"
