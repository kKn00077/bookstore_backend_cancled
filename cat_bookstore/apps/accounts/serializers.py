from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.profiles.models import UserProfile, OwnerUserProfile
from .models import UserCertification
from random import randint
from django.utils import timezone
from datetime import timedelta

UserAccount = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["email", "phone", "password"]

    def validate(self, attrs):
        """
        계정 생성 시 유효성 체크
        """

        return super().validate(attrs)

    def create(self, validated_data):
        """
        계정 생성
        """

        is_owner = validated_data["is_owner"]
        del validated_data["is_owner"]

        account = self.set_instance(validated_data, is_owner)

        account.save()
        return account

    def update(self, instance, validated_data):
        """
        계정 정보 업데이트
        """

        return super().update(instance, validated_data)

    def set_instance(self, data, is_owner):
        """
        UserAccount 데이터와
        Profile 데이터를 세팅해서 인스턴스를 리턴해줌
        """

        account = UserAccount(**data)
        account.set_password(account.password)

        if is_owner:
            account.owner_profile = OwnerUserProfile()
        else:
            account.profile = UserProfile()

        return account


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


class UserCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCertification
        fields = "__all__"
