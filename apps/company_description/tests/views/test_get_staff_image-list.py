from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class StaffImageApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_staff_images_url = reverse("staff-image-list")

    def test_staff_image_list_api(self):
        """
        Ensure we can get staff images list.
        """
        response = self.client.get(self.get_staff_images_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
