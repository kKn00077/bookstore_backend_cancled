from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CategorySerializer, BookstoreSerializer
from .models import Category, Bookstore

class BookstoreAppViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
        서점 관련 정보 viewset (App 내에서)
    """

    # 기본 쿼리셋
    queryset = Bookstore.objects.all().order_by("-bookstore_id")

    # 사용되는 serializer 클래스
    serializer_class = BookstoreSerializer
    
    # 해당 viewset에서 사용되는 기본 권한
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = self.queryset

        category = self.request.query_params.get('category', None)

        if category is not None:
            pass
            # queryset = queryset.filter(status=status)

        return queryset

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def get_bookstore_list(self, request):
        """
            TODO: 서점 리스트를 내려줌
        """
        
        response = self.list(request)
        
        return response


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
