from django.test import tag
from rest_framework import status
from model_bakery import baker
from django.utils import timezone
from datetime import timedelta

from utils.test import APITestCase


@tag("certification", "check_code")
class CheckCodeTestCase(APITestCase):
    def setUp(self):
        certification = baker.make_recipe("apps.accounts.certification")
        certification.save()

        url = f'/certification/{certification.certification_id}/check_certification/'
        self.url = url
        self.certification = certification

    @tag("fail")
    def test_check_certification_without_data(self):
        self.post(self.url, data={}, expect_status=status.HTTP_400_BAD_REQUEST)

    @tag("fail")
    def test_check_certification_timed_out(self):
        self.certification.limit_time = timezone.now() - timedelta(seconds=1)
        self.certification.save()
        self.post(
            self.url, 
            data={"code":self.certification.code}, 
            expect_status=status.HTTP_401_UNAUTHORIZED
        )

    @tag("fail")
    def test_check_certification_code_not_match(self):
        self.post(self.url, data={"code":"111111"}, expect_status=status.HTTP_403_FORBIDDEN)

    @tag("fail")
    def test_check_certification_already_certified(self):
        self.certification.is_verified = True
        self.certification.save()
        self.post(
            self.url,
            data={"code":self.certification.code},
            expect_status=status.HTTP_403_FORBIDDEN
        )

    @tag("success")
    def test_check_certification_with_code(self):
        self.post(
            self.url,
            data={"code":self.certification.code},
        )