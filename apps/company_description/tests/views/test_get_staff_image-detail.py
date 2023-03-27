from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_staff_image


class StaffImageDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_staff_image_url = lambda pk: reverse("staff-image-detail", args=[pk])

    def test_staff_image_detail_api(self):
        """
        Ensure we can get staff image detail.
        """
        staff_image = create_test_staff_image()
        response = self.client.get(self.get_staff_image_url(staff_image.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
