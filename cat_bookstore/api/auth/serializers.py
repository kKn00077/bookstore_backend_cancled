from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework import fields
from rest_framework import exceptions
from rest_framework.serializers import Serializer, ValidationError
from rest_framework_simplejwt.tokens import AccessToken

from apps.accounts.models import UserAccount
from apps.profiles.models import UserProfile, OwnerUserProfile


class LoginSerializer(Serializer):
    email = fields.EmailField(label="이메일", write_only=True, required=False)
    phone = fields.CharField(label="전화번호", write_only=True, required=False)
    password = fields.CharField(label="비밀번호", write_only=True)

    token = fields.CharField(label="토큰", read_only=True)

    is_crm = fields.BooleanField(label="CRM 로그인 여부", write_only=True, default=False)

    def validate(self, attrs):
        email = attrs.get("email")
        phone = attrs.get("phone")

        if not email and not phone:
            raise ValidationError("phone or email is required.")

        user = authenticate(**attrs)
        
        if user is None:
            raise exceptions.AuthenticationFailed("check your account.")

        token = AccessToken.for_user(user)
        attrs["token"] = token

        return attrs


class SignupSerializer(Serializer):
    email = fields.EmailField(label="이메일", required=False)
    phone = fields.CharField(label="전화번호", required=False)
    password = fields.CharField(label="비밀번호")
    is_owner = fields.BooleanField(label="사장님 여부", default=False)

    def validate(self, attrs):
        email = attrs.get("email")
        phone = attrs.get("phone")

        if not email and not phone:
            raise ValidationError("phone or email is required.")

        return attrs

    def save(self):
        data = self.validated_data
        is_owner = data.pop('is_owner')

        user = UserAccount(**data)
        user.set_password(user.password)
        user.save()

        if is_owner:
            OwnerUserProfile.objects.create(account=user)
        else:
            UserProfile.objects.create(account=user)

        return user
