from django.test import TestCase
from rest_framework.test import APIClient

from apps.company_description.models import InformedPatientConsent
from apps.company_description.tests.utils import create_test_informed_patient_consent


class InformedPatientConsentTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_informed_patient_consent(self):
        """
        Ensure we can create informed patient consent.
        """
        informed_patient_consent = create_test_informed_patient_consent()
        self.assertTrue(isinstance(informed_patient_consent, InformedPatientConsent))
        self.assertEqual(len(InformedPatientConsent.objects.all()), 1)
