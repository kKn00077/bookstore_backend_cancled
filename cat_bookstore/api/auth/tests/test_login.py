from django.test import tag
from django.urls import reverse
from rest_framework import status
from model_bakery import baker

from utils.test import APITestCase


@tag("auth", "login")
class LoginTestCase(APITestCase):
    def setUp(self):
        user = baker.make_recipe("apps.accounts.active_user")
        url = reverse("api:auth:login")

        self.user = user
        self.url = url

    def test_login_without_data(self):
        self.post(self.url, data={}, expect_status=status.HTTP_400_BAD_REQUEST)
