from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.employees.tests.utils import create_test_junior_medical_staff


class JuniorMedicalStaffDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_junior_medical_staff_url = lambda pk: reverse(
            "junior-medical-staff-detail", args=[pk]
        )

    def test_junior_medical_staff_detail_api(self):
        """
        Ensure we can get junior medical staff detail.
        """
        junior_medical_staff = create_test_junior_medical_staff()
        response = self.client.get(
            self.get_junior_medical_staff_url(junior_medical_staff.id)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
