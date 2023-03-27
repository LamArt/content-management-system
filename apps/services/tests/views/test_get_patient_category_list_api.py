from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class PatientNeedsListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_patient_needs_url = reverse("patient-category-list")

    def test_patient_needs_list_api(self):
        """
        Ensure we can get patient needs category list.
        """
        response = self.client.get(self.get_patient_needs_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
