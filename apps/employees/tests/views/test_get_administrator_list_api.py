from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class AdministratorListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_administrators_url = reverse("administrator-list")

    def test_administrator_list_api(self):
        """
        Ensure we can get administrators list.
        """
        response = self.client.get(self.get_administrators_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
