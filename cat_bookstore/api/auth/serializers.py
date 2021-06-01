from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework import fields
from rest_framework.serializers import Serializer, ValidationError
from rest_framework_simplejwt.tokens import AccessToken


class LoginSerializer(Serializer):
    email = fields.EmailField(label="이메일", write_only=True, required=False)
    phone = fields.CharField(label="전화번호", write_only=True, required=False)
    password = fields.CharField(label="비밀번호", write_only=True)

    token = fields.CharField(label="토큰", read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        phone = attrs.get("phone")

        if not email and not phone:
            raise ValidationError("phone or email is required.")

        user = authenticate(**attrs)
        if user is None:
            raise ValidationError("check your account.")

        token = AccessToken.for_user(user)
        attrs["token"] = token

        return attrs
