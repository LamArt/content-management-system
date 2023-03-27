from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.services.tests.utils import create_test_service_file


class ServiceFileDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_service_file_url = lambda pk: reverse("service-file-detail", args=[pk])

    def test_service_file_detail_api(self):
        """
        Ensure we can get service file detail.
        """
        service_file = create_test_service_file()
        response = self.client.get(self.get_service_file_url(service_file.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
