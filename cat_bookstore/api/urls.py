from django.urls import path, include

from rest_framework import routers
from apps.files.views import FileViewset
from apps.meetings.views import MeetingCRMViewSet, MeetingCommonViewset
from apps.bookstores.views import CategoryViewSet

router = routers.SimpleRouter()
router.register(r"upload", FileViewset)
router.register(r"crm/meetings", MeetingCRMViewSet)
router.register(r"common/meetings", MeetingCommonViewset)
router.register(r"category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls))
]
