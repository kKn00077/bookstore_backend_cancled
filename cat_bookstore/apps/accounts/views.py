from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, mixins, viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import UserAccount
from .serializers import UserAccountSerializer, UserAccountLoginSerializer


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
    def register(self, request):
        """
            회원가입
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        token_result = UserAccountLoginSerializer.login(request.data)
        
        return Response(token_result, status=status.HTTP_201_CREATED)


    @action(methods=['POST'], detail=False)
    def login(self, request):
        """
            로그인
        """
        serializer = UserAccountLoginSerializer(data=request.data)
        serializer.is_valid()
        token_result = serializer.login(serializer.data)

        if token_result is None:
            return Response({"message": "fail"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(token_result, status=status.HTTP_200_OK)