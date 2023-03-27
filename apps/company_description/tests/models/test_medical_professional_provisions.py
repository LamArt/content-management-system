from django.test import TestCase
from rest_framework.test import APIClient

from apps.company_description.models import MedicalProfessionalProvisions
from apps.company_description.tests.utils import create_test_medical_professional_provisions


class MedicalProfessionalProvisionsTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_medical_professional_provisions(self):
        """
        Ensure we can create medical professional provisions.
        """
        medical_professional_provisions = create_test_medical_professional_provisions()
        self.assertTrue(
            isinstance(medical_professional_provisions, MedicalProfessionalProvisions)
        )
        self.assertEqual(len(MedicalProfessionalProvisions.objects.all()), 1)
