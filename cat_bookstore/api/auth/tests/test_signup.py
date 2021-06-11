from django.test import tag
from django.urls import reverse
from rest_framework import status
from model_bakery import baker

from utils.test import APITestCase


@tag("auth", "signup")
class SignupTestCase(APITestCase):
    def setUp(self):
        user = baker.make_recipe("apps.accounts.active_user")
        url = reverse("api:auth:signup")

        self.user = user
        self.url = url

    @tag("fail")
    def test_signup_without_data(self):
        self.post(self.url, data={}, expect_status=status.HTTP_400_BAD_REQUEST)

    @tag("fail")
    def test_signup_with_exist_email(self):
        self.post(
            self.url,
            data={"email": self.user.email, "password": "test1234"},
            expect_status=status.HTTP_400_BAD_REQUEST,
        )

    @tag("success")
    def test_signup(self):
        test_email = "test@gmail.com"
        test_password = "test1234"
        self.post(self.url, data={"email": test_email, "password": test_password}, expect_status=status.HTTP_201_CREATED)

        login_url = reverse("api:auth:login")
        self.post(login_url, data={"email": test_email, "password": test_password})
