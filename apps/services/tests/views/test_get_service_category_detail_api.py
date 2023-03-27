from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.services.tests.utils import create_test_service_category


class ServiceCategoryDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_service_category_url = lambda pk: reverse(
            "service-category-detail", args=[pk]
        )

    def test_service_category_detail_api(self):
        """
        Ensure we can get service category detail.
        """
        service_category = create_test_service_category()
        response = self.client.get(self.get_service_category_url(service_category.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
