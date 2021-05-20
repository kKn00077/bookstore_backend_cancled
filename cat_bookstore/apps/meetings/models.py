from django.db import models
from model_utils.fields import StatusField, AutoCreatedField
from model_utils.choices import Choices
from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model

UserAccount = get_user_model()

class Meeting(TimeStampedModel):
    """
    등록된 모임 정보
    """

    # 모임 신청 상태 값
    # 'CAN_APPLY' - 신청가능, 'FULL' - 만원 마감, 'CANT_APPLY' - 모집 마감(사장님이 중단하거나, 기간 만료일 경우)
    STATUS = Choices("CAN_APPLY", "FULL", "CANT_APPLY")

    meeting_id = models.AutoField(primary_key=True)

    account = models.ForeignKey(
        UserAccount,
        verbose_name="사장님 계정 정보",
        on_delete=models.CASCADE
    )

    bookstore = models.ForeignKey(
        "bookstores.Bookstore",
        verbose_name="서점 정보",
        on_delete=models.CASCADE
    )

    img_file_group = models.ForeignKey(
        "files.FileGroup",
        verbose_name="모임 이미지 묶음 파일 정보",
        null=True,
        on_delete=models.SET_NULL,
        db_column="img_file_group_id",
    )

    name = models.CharField("모임 이름", max_length=30)
    introduction = models.CharField("모임 설명", max_length=500)
    people_max_cnt = models.IntegerField("모임 인원 제한")
    metting_type = models.CharField("모임 종류", max_length=30)

    price = models.IntegerField("모임 가격")

    meeting_date = models.DateField("모임 날짜")
    start_time = models.TimeField("모임 시작 시간")
    end_time = models.TimeField("모임 종료 시간")

    status = StatusField(
        verbose_name="모임 신청 상태",
        max_length=30,
        default=STATUS.CAN_APPLY,
        help_text="CAN_APPLY - 신청가능 / FULL - 만원 마감 / CANT_APPLY - 모집 마감(사장님이 중단하거나, 기간 만료일 경우)",
    )

    apply_users = models.ManyToManyField(
        UserAccount, through="MeetingAttendApply", related_name="apply_meeting"
    )

    class Meta:
        ordering = ["-meeting_id"]

        verbose_name = "모임"
        verbose_name_plural = "모임"

    def __str__(self):
        return f"{self.name} - {self.bookstore}"


class MeetingAttendApply(models.Model):
    """
    등록된 모임 정보
    """

    # 모임 신청 상태 값
    # WAITTING - 대기 / ACCEPTED - 수락 / CANCLED - 취소 / FAILED - 실패 (에러 등으로)
    STATUS = Choices("WAITTING", "ACCEPTED", "CANCLED", "FAILED")

    apply_id = models.AutoField(primary_key=True)

    meeting = models.ForeignKey(
        Meeting, verbose_name="모임 정보", on_delete=models.CASCADE
    )

    account = models.ForeignKey(
        UserAccount,
        verbose_name="신청한 유저의 계정 정보",
        on_delete=models.CASCADE
    )

    status = StatusField(
        max_length=30,
        verbose_name="신청 상태",
        default=STATUS.WAITTING,
        help_text="WAITTING - 대기 / ACCEPTED - 수락 / CANCLED - 취소 / FAILED - 실패 (에러 등으로)",
    )

    err_msg = models.CharField("에러 메세지", max_length=500)

    apply_date = AutoCreatedField("신청 일시")

    class Meta:
        ordering = ["-apply_id"]

        verbose_name = "모임 참가 신청"
        verbose_name_plural = "모임 참가 신청"

    def __str__(self):
        return f"{self.meeting} - {self.account}"
