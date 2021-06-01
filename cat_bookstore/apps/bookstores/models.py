from apps.books.models import Books
from apps.products.models import BookStock
from apps.profiles.models import CategorySubscribe
from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model

UserAccount = get_user_model()
class Bookstore(TimeStampedModel):
    """
    서점 정보 관련
    """

    bookstore_id = models.AutoField(primary_key=True)

    """
    #서점과 사장님의 관계는 1:N이 맞지만 일단 계정당 1개의 서점을 배치함(1:1)
    #수요가 늘 경우 1:N으로 변경
    #계정이 삭제돼도 서점정보는 남겨야 하므로 null=True 설정
    account = models.ForeignKey(
        UserAccount,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="사장님 계정 정보",
        db_column="account_id",
    )
    """
    account = models.OneToOneField(
        UserAccount,
        verbose_name="유저 계정 정보",
        null=True,
        on_delete=models.SET_NULL,
        related_name="bookstore"
    )

    img_file_group = models.ForeignKey(
        "files.FileGroup",
        verbose_name="서점 이미지 묶음 파일 정보",
        null=True,
        on_delete=models.SET_NULL
    )

    name = models.CharField("서점명", max_length=30)
    address = models.CharField("서점 주소", max_length=100)
    address_detail = models.CharField("서점 상세 주소", max_length=100)
    introduction = models.TextField("서점 소개", blank=True)

    start_time = models.TimeField("영업 시작 시간")
    end_time = models.TimeField("영업 끝나는 시간")

    is_affiliate = models.BooleanField("가맹점 여부", default=False)

    # 서점 구독 유저
    subscribed_users = models.ManyToManyField(
        UserAccount, through="SubscribeInfo", related_name="subscribed"
    )
    
    # 서점 좋아요
    liked_users = models.ManyToManyField(
        UserAccount, through="UserLikedBookstore", related_name="liked"
    )

    # 서점 책 재고
    book_stock = models.ManyToManyField(
        Books, through=BookStock, related_name="bookstore"
    )

    class Meta:
        ordering = ["-bookstore_id"]

        verbose_name = "서점 정보"
        verbose_name_plural = "서점 정보"

    def __str__(self):
        return f"{self.name} - {self.address}"


class BookstoreCategory(models.Model):
    """
    서점 카테고리
    (심리학 전문 서점인지, 고전 문학 전문 서점인지 등등..)

    서점의 카테고리는 여러개일 수 있음
    """

    bookstores_category_id = models.AutoField(primary_key=True)

    bookstore = models.ForeignKey(
        Bookstore,
        verbose_name="서점",
        on_delete=models.CASCADE
    )

    # default = 1 -> 기타 카테고리
    category = models.ForeignKey(
        "Category",
        verbose_name="카테고리",
        on_delete=models.SET_DEFAULT,
        default=1
    )

    class Meta:
        ordering = ["-bookstores_category_id"]

        verbose_name = "서점 카테고리"
        verbose_name_plural = "서점 카테고리"

    def __str__(self):
        return f"{self.bookstore} - {self.category_type}"


class Category(models.Model):
    """
    카테고리 분류
    """

    category_id = models.AutoField(primary_key=True)
    name = models.CharField("카테고리명", max_length=30)

    # 서점 카테고리
    bookstore = models.ManyToManyField(
        Bookstore, through=BookstoreCategory, related_name="category"
    )

    # 카테고리 구독 사용자
    account = models.ManyToManyField(
        UserAccount, through=CategorySubscribe, related_name="subscribe_category"
    )

    class Meta:
        ordering = ["-category_id"]

        verbose_name = "카테고리 분류"
        verbose_name_plural = "카테고리 분류"

    def __str__(self):
        return f"{self.name}"



class SubscribeInfo(models.Model):
    """
    사용자 구독 정보
    """

    subscribe_id = models.AutoField(primary_key=True)

    account = models.ForeignKey(
        UserAccount,
        verbose_name="사용자 계정 정보",
        on_delete=models.CASCADE
    )

    bookstore = models.ForeignKey(
        Bookstore,
        verbose_name="서점 정보",
        on_delete=models.CASCADE
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
        UserAccount,
        verbose_name="사용자 계정 정보",
        null=True,
        on_delete=models.SET_NULL
    )

    bookstore = models.ForeignKey(
        Bookstore,
        verbose_name="서점 정보",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-liked_id"]

        verbose_name = "사용자 좋아요 현황"
        verbose_name_plural = "사용자 좋아요 현황"

        unique_together = (("account", "bookstore"),)

    def __str__(self):
        return f"{self.account} - {self.bookstore}"
