from rest_framework import serializers
from django.contrib.auth import get_user_model
from random import randint
from django.utils import timezone
from datetime import timedelta

UserAccount = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"


class SendCodeSerializer(serializers.Serializer):
    """
    유저 계정 생성 전 인증코드 관련 로직 수행 시리얼라이저
    sms 인증 코드 생성/발송, email 인증 코드 생성/발송
    """

    is_email_cerifiation = serializers.BooleanField(default=False, write_only=True)

    email = serializers.EmailField(
        max_length=255, required=False, allow_null=True, write_only=True
    )
    phone = serializers.CharField(
        max_length=11, required=False, allow_null=True, write_only=True
    )

    sms_code = serializers.IntegerField(read_only=True)
    sms_time_limit = serializers.DateTimeField(read_only=True)

    email_code = serializers.IntegerField(read_only=True)
    email_time_limit = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        is_email_cerifiation = attrs.get("is_email_cerifiation")
        email = attrs.get("email", None)
        phone = attrs.get("phone", None)

        if is_email_cerifiation:
            if email is None:
                raise serializers.ValidationError("email is None")
        else:
            if phone is None:
                raise serializers.ValidationError("phone is None")

        return attrs

    def send_code(self):
        is_email_cerifiation = self.validated_data["is_email_cerifiation"]
        code = f"{randint(100000, 999999)}"
        limit_time = timezone.now() + timedelta(minutes=3)

        # TODO: 발송 로직
        if is_email_cerifiation:
            self.validated_data["email_code"] = code
            self.validated_data["email_time_limit"] = limit_time
        else:
            self.validated_data["sms_code"] = code
            self.validated_data["sms_time_limit"] = limit_time
