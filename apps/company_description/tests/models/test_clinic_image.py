from django.test import TestCase
from rest_framework.test import APIClient

from apps.company_description.models import CompanyImage
from apps.company_description.tests.utils import create_test_company_image


class ClinicImageTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_clinic_image_create(self):
        """
        Ensure we can create clinic image.
        """
        clinic_image = create_test_company_image()
        self.assertTrue(isinstance(clinic_image, CompanyImage))
        self.assertEqual(len(CompanyImage.objects.all()), 1)
