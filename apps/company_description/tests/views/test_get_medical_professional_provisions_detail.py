from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import (
    create_test_medical_professional_provisions,
)


class MedicalProfessionalProvisionsDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_medical_professional_provisions_url = lambda pk: reverse(
            "medical-professional-provisions-detail", args=[pk]
        )

    def test_medical_professional_provisions_detail_api(self):
        """
        Ensure we can get medical professional provisions detail.
        """
        medical_professional_provisions = create_test_medical_professional_provisions()
        response = self.client.get(
            self.get_medical_professional_provisions_url(
                medical_professional_provisions.id
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
