from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class JuniorStaffListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_junior_staff_url = reverse("junior-staff-list")

    def test_junior_staff_list_api(self):
        """
        Ensure we can get junior staff list.
        """
        response = self.client.get(self.get_junior_staff_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
