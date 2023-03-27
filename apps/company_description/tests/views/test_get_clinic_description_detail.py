from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_clinic_description


class ClinicDescriptionDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_clinic_description_url = lambda pk: reverse(
            "clinic-description-detail", args=[pk]
        )

    def test_clinic_description_detail_api(self):
        """
        Ensure we can get clinic description detail.
        """
        clinic_description = create_test_clinic_description()
        response = self.client.get(
            self.get_clinic_description_url(clinic_description.id)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
