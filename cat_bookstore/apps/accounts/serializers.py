from .models import Certification
from rest_framework import serializers
from django.contrib.auth import get_user_model
from random import randint
from django.utils import timezone
from datetime import timedelta
from .enums import CertificationTypeChoice
from apps.utils.exceptions import AppExceptions

UserAccount = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"


class CertificationSerializer(serializers.ModelSerializer):
    """
    유저 계정 생성 전 인증코드 관련 로직 수행 시리얼라이저
    sms 인증 코드 생성/발송, email 인증 코드 생성/발송
    """

    class Meta:
        model = Certification
        fields = "__all__"
        extra_kwargs = {
            'certification_type': {'required': False},
            'code': {'required': False},
            'limit_time': {'required': False, 'write_only':True},
            'address': {'required': False, 'write_only':True}
        }


    email = serializers.EmailField(
        max_length=255, required=False, allow_null=True, write_only=True
    )
    phone = serializers.CharField(
        max_length=11, required=False, allow_null=True, write_only=True
    )

    def validate(self, attrs):
        """
        create 일때는 email이나 phone 정보 필수
        update 일때는 pk랑 code 정보 필수
        """
        if self.instance is None:
            email = attrs.get("email", None)
            phone = attrs.get("phone", None)
            
            if not email and not phone:
                raise serializers.ValidationError("phone or email is required.")
        else:
            code = attrs.get('code', None)
            
            if self.instance.is_verified:
                raise AppExceptions.AlreadyCertified()

            if not code:
                raise serializers.ValidationError("code is required.")

            if timezone.now() > self.instance.limit_time:
                raise AppExceptions.CertificationTimedOut()

            if code != self.instance.code:
                raise AppExceptions.CertificationCodeNotMatch()

        return attrs

    def create(self, validated_data):

        email = validated_data.pop("email", None)
        phone = validated_data.pop("phone", None)
        code = f"{randint(100000, 999999)}"
        limit_time = timezone.now() + timedelta(minutes=3)
        
        if phone is not None:
            validated_data["certification_type"] = CertificationTypeChoice.SMS
            validated_data["address"] = phone
        else:
            validated_data["certification_type"] = CertificationTypeChoice.EMAIL
            validated_data["address"] = email

        validated_data["code"] = code
        validated_data["limit_time"] = limit_time

        # TODO: 발송 로직 추가

        certification = Certification(**validated_data)
        certification.save()

        return certification

    def update(self, instance, validated_data):
        instance.is_verified=True
        instance.save()
        return instance
