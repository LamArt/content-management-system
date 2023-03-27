from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.services.tests.utils import (
    create_test_service,
    create_test_service_category,
)


class ServiceDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_service_url = lambda pk: reverse("service-detail", args=[pk])
        self.service_category = create_test_service_category()

    def test_service_detail_api(self):
        """
        Ensure we can get service detail.
        """
        service = create_test_service(service_category=self.service_category)
        response = self.client.get(self.get_service_url(service.slug))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
