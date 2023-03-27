from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.services.tests.utils import (
    create_test_service_patient_needs_category,
)


class PatientNeedsDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_patient_needs_url = lambda pk: reverse(
            "patient-category-detail", args=[pk]
        )

    def test_patient_needs_detail_api(self):
        """
        Ensure we can get patient needs category detail.
        """
        patient_needs_category = create_test_service_patient_needs_category()
        response = self.client.get(
            self.get_patient_needs_url(patient_needs_category.id)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
