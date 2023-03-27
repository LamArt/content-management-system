from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class PatientInfoApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_patient_info_url = reverse("patient-info-list")

    def test_patient_info_list_api(self):
        """
        Ensure we can get patient info list.
        """
        response = self.client.get(self.get_patient_info_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
