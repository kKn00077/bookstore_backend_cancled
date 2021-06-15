from django.test import tag
from rest_framework import status
from model_bakery import baker

from utils.test import APITestCase


@tag("meeting", "register")
class RegisterTestCase(APITestCase):
    def setUp(self):
        user = baker.make_recipe("apps.accounts.active_user")
        profile = baker.prepare("profiles.OwnerUserProfile", account=user)
        bookstore = baker.prepare("bookstores.Bookstore", account=user)

        meeting = baker.make_recipe("apps.meetings.meeting")

        url = '/crm/meetings/register/'

        user.save()
       
        self.url = url
        self.user = user
        self.profile = profile
        self.bookstore = bookstore
        self.meeting = meeting

    @tag("fail")
    def test_meeting_register_without_user(self):
        self.post(self.url, data={}, expect_status=status.HTTP_401_UNAUTHORIZED)

    @tag("fail")
    def test_meeting_register_not_owner(self):
        self.post(self.url, data={}, user=self.user, expect_status=status.HTTP_403_FORBIDDEN)

    @tag("fail")
    def test_meeting_register_is_owner_without_data(self):
        self.profile.save()
        self.bookstore.save()
        self.post(self.url, data={}, user=self.user, expect_status=status.HTTP_400_BAD_REQUEST)

    @tag("success")
    def test_meeting_register_is_owner_with_data(self):
        self.profile.save()
        self.bookstore.save()
        self.post(
            self.url,
            data={
                "img_file_group":self.meeting.img_file_group.file_group_id,
                "name":self.meeting.name,
                "introduction":self.meeting.introduction,
                "people_max_cnt":self.meeting.people_max_cnt,
                "metting_type":self.meeting.metting_type,
                "price":self.meeting.price,
                "meeting_date":self.meeting.meeting_date,
                "start_time":self.meeting.start_time,
                "end_time":self.meeting.end_time,
                "status":self.meeting.status
            }, 
            user=self.user, 
            expect_status=status.HTTP_201_CREATED
        )