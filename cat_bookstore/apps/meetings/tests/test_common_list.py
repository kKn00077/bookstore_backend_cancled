from django.test import tag
from rest_framework import status
from model_bakery import baker

from utils.test import APITestCase


@tag("meeting", "list")
class MeetingListTestCase(APITestCase):
    def setUp(self):
        user = baker.make_recipe("apps.accounts.active_user")
        meeting = baker.make_recipe("apps.meetings.meeting")
        
        user.save()
        meeting.save()

        url = '/common/meetings/get_meeting_list/'

        self.url = url
        self.user = user

    @tag("fail")
    def test_meeting_list_without_user(self):
        self.get(self.url, data={}, expect_status=status.HTTP_401_UNAUTHORIZED)

    @tag("success")
    def test_meeting_list_with_user(self):
        self.get(self.url, data={}, has_pagination=True, user=self.user)

    @tag("success")
    def test_meeting_list_with_user_set_filter(self):
        self.get(self.url, data={"status":"CAN_APPLY"}, has_pagination=True, user=self.user)