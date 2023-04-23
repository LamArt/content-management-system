from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class CompanyImageApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_company_images_url = reverse("company-image-list")

    def test_company_image_list_api(self):
        """
        Ensure we can get company images list.
        """
        response = self.client.get(self.get_company_images_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
