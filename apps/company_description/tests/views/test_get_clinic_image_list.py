from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ClinicImageApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_clinic_images_url = reverse("clinic-image-list")

    def test_clinic_image_list_api(self):
        """
        Ensure we can get clinic images list.
        """
        response = self.client.get(self.get_clinic_images_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
