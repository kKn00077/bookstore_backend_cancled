from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, mixins, viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import UserAccount


class AccountViewSet(viewsets.GenericViewSet):
    queryset = UserAccount.objects.all()
    permission_classes = [AllowAny]

    @action(methods=['POST'], detail=False)
    def register(self, request):
        """
            회원가입
        """

        pass