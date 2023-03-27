from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ServiceListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_portfolio_url = reverse("portfolio-list")

    def test_portfolio_list_api(self):
        """
        Ensure we can get portfolio list.
        """
        response = self.client.get(self.get_portfolio_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
