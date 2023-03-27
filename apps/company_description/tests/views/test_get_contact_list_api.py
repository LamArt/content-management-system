from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ContactListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_contacts_url = reverse("contact-list")

    def test_contacts_list_api(self):
        """
        Ensure we can get contacts list.
        """
        response = self.client.get(self.get_contacts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
