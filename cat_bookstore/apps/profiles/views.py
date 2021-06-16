from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CategorySubscribe
from .serializers import CategorySubscribeSerializer

class CategorySubscribeViewset(viewsets.GenericViewSet,
                                mixins.CreateModelMixin):
    """
        유저 카테고리 구독 작업 관련 viewset
    """

    # 쿼리셋
    queryset = CategorySubscribe.objects.all()

    # 사용되는 serializer 클래스
    serializer_class = CategorySubscribeSerializer

    # 해당 viewset에서 사용되는 기본 권한
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        사용자 카테고리 구독 정보 생성
        user의 경우 엔드포인트 자체에서 auth 여부를 판단해서 예외를 던져주기 때문에
        시리얼라이저에 필수 필드가 아닌 context 필드로 넘겨줌
        (인증이 될 경우 프론트에서 넘겨준 사용자값이 아니라 인증된 사용자의 정보를 사용하기 때문임)
        
        (왜냐하면 many=True로 설정해놨기 때문에 시리얼라이저에 필드를 해놓을 경우 데이터 포매팅 코드를
        따로 구현을 해야하기 때문임.)
        """

        serializer = self.get_serializer(data=request.data, context={'user':request.user}, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['POST'], detail=False)
    def create_subscribe_category(self, request):
        """
        카테고리 구독 정보 생성
        """
        response = self.create(request)
        
        return response
