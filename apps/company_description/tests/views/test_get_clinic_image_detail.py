from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_clinic_image


class ClinicImageDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_clinic_image_url = lambda pk: reverse("clinic-image-detail", args=[pk])

    def test_clinic_image_detail_api(self):
        """
        Ensure we can get clinic image detail.
        """
        clinic_image = create_test_clinic_image()
        response = self.client.get(self.get_clinic_image_url(clinic_image.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
