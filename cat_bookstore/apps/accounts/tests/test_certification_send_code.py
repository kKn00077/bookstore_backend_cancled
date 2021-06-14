from django.test import tag
from django.urls import reverse
from rest_framework import status
from model_bakery import baker

from utils.test import APITestCase


@tag("certification", "send_code")
class SendCodeTestCase(APITestCase):
    def setUp(self):
        url = '/certification/send_certification_code/'
        self.url = url

    @tag("fail")
    def test_send_certification_code_without_data(self):
        self.post(self.url, data={}, expect_status=status.HTTP_400_BAD_REQUEST)

    @tag("success")
    def test_send_certification_code_with_phone(self):
        self.post(
            self.url,
            data={"phone": "01011111111"},
            expect_status=status.HTTP_201_CREATED,
        )

    @tag("success")
    def test_send_certification_code_with_email(self):
        self.post(
            self.url,
            data={"email": "test@test.co.kr"},
            expect_status=status.HTTP_201_CREATED,
        )
