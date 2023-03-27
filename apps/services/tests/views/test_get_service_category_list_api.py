from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ServiceCategoryListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_service_category_url = reverse("service-category-list")

    def test_service_category_list_api(self):
        """
        Ensure we can get service category list.
        """
        response = self.client.get(self.get_service_category_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
