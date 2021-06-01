from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
        카테고리 정보 viewset
    """

    # 기본 쿼리셋
    queryset = Category.objects.all().order_by("-category_id")

    # 사용되는 serializer 클래스
    serializer_class = CategorySerializer
    
    # 해당 viewset에서 사용되는 기본 권한
    permission_classes = [AllowAny]

    # pagination 없이 전부 내려줄 거기 때문에 None으로 설정
    pagination_class = None

    @action(methods=['GET'], detail=False)
    def category_list(self, request):
        """
            카테고리 리스트를 내려줌
        """
        
        response = self.list(request)
        
        return response
