from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import FileUploadSerializer
from .models import File, FileGroup

class FileViewset(viewsets.GenericViewSet):
    """
        파일 작업 관련 viewset
    """

    # 기본 쿼리셋
    queryset = File.objects.all()

    # 사용되는 serializer 클래스
    serializer_class = FileUploadSerializer

    # 해당 viewset에서 사용되는 기본 권한
    permission_classes = [AllowAny]

    # 파서 클래스 정의 (파일 관련 파서)
    parser_classes = [MultiPartParser, FormParser]

    @action(methods=['POST'], detail=False)
    def upload_file(self, request):
        """
            TODO: 단일 파일 업로드
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(status=status.HTTP_201_CREATED)


    @action(methods=['POST'], detail=False)
    def upload_file_group(self, request):
        """
            TODO: 묶음 파일 업로드
        """
        
        return Response(status=status.HTTP_201_CREATED)