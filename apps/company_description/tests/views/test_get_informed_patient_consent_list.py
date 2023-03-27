from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class InformedPatientConsentApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_informed_patient_consent_url = reverse("informed-patient-consent-list")

    def test_informed_patient_consent_list_api(self):
        """
        Ensure we can get informed patient consent list.
        """
        response = self.client.get(self.get_informed_patient_consent_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
