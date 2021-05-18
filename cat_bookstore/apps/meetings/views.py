from apps.accounts.permissions import IsOwnerAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import MeetingSerializer
from .models import Meeting


class MeetingViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
        미팅 관련 관리하는 viewset
    """

    # 기본 쿼리셋
    queryset = Meeting.objects.all()

    # 사용되는 serializer 클래스
    serializer_class = MeetingSerializer

    # 해당 viewset에서 사용되는 기본 권한
    permission_classes = [IsOwnerAuthenticated]

    @action(methods=['POST'], detail=False)
    def register(self, request):
        """
            미팅 등록

            TODO: file 등록
        """
        account = request.user
        bookstore = account.bookstore_set.first()

        request.data['account'] = account.account_id
        request.data['bookstore'] = bookstore.bookstore_id

        response = self.create(request)
        
        return response