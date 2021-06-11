from django.test import tag
from django.urls import reverse
from rest_framework import status
from model_bakery import baker

from utils.test import APITestCase


@tag("auth", "login")
class LoginTestCase(APITestCase):
    def setUp(self):
        user = baker.make_recipe("apps.accounts.active_user")
        user.set_password("test1234")
        user.save()

        url = reverse("api:auth:login")

        self.user = user
        self.url = url

    @tag("fail")
    def test_login_without_data(self):
        self.post(self.url, data={}, expect_status=status.HTTP_400_BAD_REQUEST)

    @tag("fail")
    def test_login_with_email_for_wrong_password(self):
        self.post(
            self.url,
            data={"email": self.user.email, "password": "test12345"},
            expect_status=status.HTTP_401_UNAUTHORIZED,
        )

    @tag("success")
    def test_login_with_email(self):
        result = self.post(
            self.url, data={"email": self.user.email, "password": "test1234"}
        )
        self.check_field_exists(result, ["token"])
        token = result["token"]
