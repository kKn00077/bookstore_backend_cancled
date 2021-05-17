from rest_framework.permissions import IsAuthenticated
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import MeetingSerializer
from .models import Meeting


class MeetingViewSet(viewsets.GenericViewSet):
    """
        계정 정보를 관리하는 viewset
    """

    # 기본 쿼리셋
    queryset = Meeting.objects.all()

    # 사용되는 serializer 클래스
    serializer_class = MeetingSerializer

    # 해당 viewset에서 사용되는 기본 권한
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=False)
    def register(self, request):
        """
            TODO:미팅 등록
        """
        
        return Response(status=status.HTTP_201_CREATED)