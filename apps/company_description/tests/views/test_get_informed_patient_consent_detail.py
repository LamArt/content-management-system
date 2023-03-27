from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_informed_patient_consent


class InformedPatientConsentDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_informed_patient_consent_url = lambda pk: reverse(
            "informed-patient-consent-detail", args=[pk]
        )

    def test_informed_patient_consent_detail_api(self):
        """
        Ensure we can get informed patient consent detail.
        """
        informed_patient_consent = create_test_informed_patient_consent()
        response = self.client.get(
            self.get_informed_patient_consent_url(informed_patient_consent.id)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
