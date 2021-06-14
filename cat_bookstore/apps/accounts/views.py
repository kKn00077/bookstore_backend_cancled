from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Certification

from .serializers import (
    CertificationSerializer,
)


class CertificationViewSet(viewsets.GenericViewSet,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin):
    """
    계정 정보를 관리하는 viewset
    """

    # 기본 쿼리셋
    queryset = Certification.objects.all()

    # 사용되는 serializer 클래스
    serializer_class = CertificationSerializer

    # 해당 viewset에서 사용되는 기본 권한
    permission_classes = [AllowAny]

    @action(methods=["POST"], detail=False)
    def send_certification_code(self, request):
        """
        인증번호 발송 및 인증정보 생성
        """
        response = self.create(request)

        return response

    @action(methods=["POST"], detail=True)
    def check_certification(self, request, pk=None):
        """
        인증번호 인증 체크
        """
        response = self.update(request)

        return response