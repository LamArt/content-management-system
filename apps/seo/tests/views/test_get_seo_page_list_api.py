from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class SEOListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_seo_url = reverse("page-list")

    def test_page_seo_list_api(self):
        """
        Ensure we can get page seo list.
        """
        response = self.client.get(self.get_seo_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
