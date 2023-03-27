from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ServiceListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_service_url = reverse("service-list")

    def test_service_list_api(self):
        """
        Ensure we can get service list.
        """
        response = self.client.get(self.get_service_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
