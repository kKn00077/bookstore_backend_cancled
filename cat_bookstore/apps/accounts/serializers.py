from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from apps.profiles.models import UserProfile, OwnerUserProfile
from .models import UserCertification
from random import randint
from django.utils import timezone
from datetime import timedelta

# JWT 사용을 위한 설정
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

UserAccount = get_user_model()

class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ['email', 'phone', 'password']


    def validate(self, attrs):
        """
            계정 생성 시 유효성 체크
        """

        return super().validate(attrs)


    def create(self, validated_data):
        """
            계정 생성
        """

        is_owner = validated_data['is_owner']
        del validated_data['is_owner']

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
    

class UserAccountLoginSerializer(serializers.ModelSerializer):
    

    # 로그인에 필요한 정보
    class Meta:
        model = UserAccount
        fields = ['email', 'phone', 'password']
        extra_kwargs = {
            'email': {"required": False, "allow_null": True},
            'phone': {"required": False, "allow_null": True},
            'password': {'write_only': True},
        }

    def validate(self, attrs):

        email = attrs.get('email', None)
        phone = attrs.get('phone', None)
        password = attrs.get('password', None)

        if email is None:
            if phone is None:
                raise serializers.ValidationError('phone is None')
        else:
            raise serializers.ValidationError('phone or email is None')
            
        if password is None:
            raise serializers.ValidationError('password is None')

        return attrs

    @classmethod
    def login(cls, data):
        
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')

        is_owner = data.get('is_owner', None)

        # 사용자 정보로 로그인 (phone 이 없을 경우 이메일 로그인 시도)
        if phone is not None:
            account = authenticate(phone=phone, password=password, is_owner=is_owner)
        else:
            account = authenticate(email=email, password=password, is_owner=is_owner)

        if account is None: 
            return None

        try: 
            payload = JWT_PAYLOAD_HANDLER(account) 
            jwt_token = JWT_ENCODE_HANDLER(payload) 
            update_last_login(None, account)
        except UserAccount.DoesNotExist: 
            raise serializers.ValidationError(
                'User with given login_id(email or phone) and password does not exist')

        return { 'token': jwt_token }


class SendCodeSerializer(serializers.Serializer):
    """
    유저 계정 생성 전 인증코드 관련 로직 수행 시리얼라이저
    sms 인증 코드 생성/발송, email 인증 코드 생성/발송
    """

    is_email_cerifiation = serializers.BooleanField(default=False, write_only=True)

    email = serializers.EmailField(max_length=255, required=False, allow_null=True, write_only=True)
    phone = serializers.CharField(max_length=11, required=False, allow_null=True, write_only=True)

    sms_code = serializers.IntegerField(read_only=True)
    sms_time_limit = serializers.DateTimeField(read_only=True)

    email_code = serializers.IntegerField(read_only=True)
    email_time_limit = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        is_email_cerifiation = attrs.get('is_email_cerifiation')
        email = attrs.get('email', None)
        phone = attrs.get('phone', None)

        if(is_email_cerifiation):
            if email is None:
                raise serializers.ValidationError('email is None')
        else:
            if phone is None:
                raise serializers.ValidationError('phone is None')

        return attrs

    def send_code(self):
        is_email_cerifiation = self.validated_data["is_email_cerifiation"]
        code = f'{randint(100000, 999999)}'
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

    