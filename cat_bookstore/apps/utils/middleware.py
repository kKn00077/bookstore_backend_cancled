from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from .enums import VersionStatusChoice
from .models import AppVersion

class AppHeaderMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)

        return response

    def process_response(self, request, response):
        ANDROID = ['android']
        IOS = ['iphone', 'ipad']
        
        user_agent=request.headers.get('User-Agent', 'undefined')
        user_agent_lower = user_agent.lower()
        
        # ANDROID 플랫폼 리스트 중에 해당되는 게 있는지
        if any(android_platform for android_platform in ANDROID if android_platform in user_agent_lower):
            platform = 'android'
        # IOS 플랫폼 리스트 중에 해당되는 게 있는지
        elif any(ios_platform for ios_platform in IOS if ios_platform in user_agent_lower):
            platform = 'ios'
        # 둘다 없으면 기존의 user_agent 그대로 담아서 보내기
        else:
            platform = user_agent

        
        response['User-Agent'] = platform
        return response


class AppUpdateCheckMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        user_agent = request.headers.get('User-Agent', 'undefined').lower()
        app_version=request.headers.get('App-Version', None)
        version_queryset = AppVersion.objects.filter(version=app_version)
        
        if 'mobile' in user_agent:
            # header값이 없거나 버전을 찾을 수 없는 경우
            if version_queryset.count() <= 0:
                return JsonResponse({"message" : "App-Version is not found in headers"},
                                        status=status.HTTP_400_BAD_REQUEST,
                                        headers={
                                            'App-Version-Status':'UNKNOWN', 
                                            'Is-Mobile' : True})
            
            # 업데이트 필수
            if version_queryset[0].status == VersionStatusChoice.UPDATE_REQUIRED:
                return JsonResponse({"message" : "App-Version is black-list"},
                                        status=status.HTTP_403_FORBIDDEN,
                                        headers={
                                            'App-Version-Status':VersionStatusChoice.UPDATE_REQUIRED, 
                                            'Is-Mobile' : True})

                

    def process_response(self, request, response):
        user_agent = request.headers.get('User-Agent', 'undefined').lower()
        status = response.get('App-Version-Status', None)
        
        if 'mobile' in user_agent:
            if status != 'UNKNOWN':
                app_version=request.headers.get('App-Version')
                version_queryset = AppVersion.objects.get(version=app_version)

                response['App-Version-Status'] = version_queryset.status

        return response