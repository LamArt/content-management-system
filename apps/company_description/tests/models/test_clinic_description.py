from django.test import TestCase
from django.db.utils import IntegrityError
from rest_framework.test import APIClient

from apps.company_description.models import ClinicDescription
from apps.company_description.tests.utils import create_test_clinic_description


class ClinicDescriptionTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_clinic_description_create(self):
        """
        Ensure we can create clinic description. Provide singleton model
        """
        clinic_description = create_test_clinic_description()
        self.assertTrue(isinstance(clinic_description, ClinicDescription))
        self.assertEqual(len(ClinicDescription.objects.all()), 1)
        self.assertRaises(IntegrityError, create_test_clinic_description)
