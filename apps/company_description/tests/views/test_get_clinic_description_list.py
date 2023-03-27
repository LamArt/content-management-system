from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ClinicDescriptionApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_clinic_description_url = reverse("clinic-description-list")

    def test_clinic_description_list_api(self):
        """
        Ensure we can get clinic description list.
        """
        response = self.client.get(self.get_clinic_description_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
