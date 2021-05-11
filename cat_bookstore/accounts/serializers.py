from rest_framework import serializers
from django.contrib.auth import get_user_model

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

        account = UserAccount(**validated_data)
        account.save()
        return account


    def update(self, instance, validated_data):
        """
            계정 정보 업데이트
        """

        return super().update(instance, validated_data)
    