from django.test import tag
from django.urls import reverse
from rest_framework import status
from model_bakery import baker

from utils.test import APITestCase


@tag("bookstores", "category")
class CategoryTestCase(APITestCase):
    def setUp(self):
        url = '/category/category_list/'
        self.url = url

    @tag("success")
    def test_get_category(self):
        self.get(self.url, data={})