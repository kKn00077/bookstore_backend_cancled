from apps.utils import exceptions
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserAccount

from .serializers import (
    UserAccountSerializer, 
    UserAccountLoginSerializer, 
    SendCodeSerializer, 
    UserCertificationSerializer
)


class UserAccountViewSet(viewsets.GenericViewSet):
    """
        계정 정보를 관리하는 viewset
    """

    # 기본 쿼리셋
    queryset = UserAccount.objects.all()

    # 사용되는 serializer 클래스
    serializer_class = UserAccountSerializer
    
    # 해당 viewset에서 사용되는 기본 권한
    permission_classes = [AllowAny]

    @action(methods=['POST'], detail=False)
    def sign_up(self, request):
        """
            회원가입

            TODO: 추후 기획에 맞춰 커스텀
        """
        is_owner = request.data.get('is_owner', False)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_owner=is_owner)
        
        token_result = UserAccountLoginSerializer.login(request.data)
        
        return Response(token_result, status=status.HTTP_201_CREATED)


    @action(methods=['POST'], detail=False)
    def login(self, request):
        """
            로그인

            TODO: 추후 기획에 맞춰 커스텀
        """
        serializer = UserAccountLoginSerializer(data=request.data)
        serializer.is_valid()
        token_result = serializer.login(serializer.data)
        if token_result is None:
            raise exceptions.CommonExceptions.UserNotFound()

        return Response(token_result, status=status.HTTP_200_OK)


    @action(methods=['POST'], detail=False)
    def send_certification_code(self, request):
        """
        인증번호 발송 및 인증정보 생성
        """

        serializer = SendCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        
        #TODO: 인증 정보 생성 (UserCertification)

        return Response(status=status.HTTP_201_CREATED)