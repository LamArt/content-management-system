from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_patient_info


class PatientInfoDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_patient_info_url = lambda pk: reverse("patient-info-detail", args=[pk])

    def test_patient_info_detail_api(self):
        """
        Ensure we can get patient info detail.
        """
        patient_info = create_test_patient_info()
        response = self.client.get(self.get_patient_info_url(patient_info.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
