from django.urls import path, include

from rest_framework import routers
from apps.meetings.views import MeetingViewSet

router = routers.SimpleRouter()
router.register(r"meetings", MeetingViewSet)

urlpatterns = [
    path("", include(router.urls))
]
