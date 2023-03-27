from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class MedicalProfessionalProvisionsApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_medical_professional_provisions_url = reverse(
            "medical-professional-provisions-list"
        )

    def test_medical_professional_provisions_list_api(self):
        """
        Ensure we can get medical professional provisions list.
        """
        response = self.client.get(self.get_medical_professional_provisions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
