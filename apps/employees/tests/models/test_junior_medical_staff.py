from django.test import TestCase
from rest_framework.test import APIClient

from apps.employees.models import JuniorMedicalStaff
from apps.employees.tests.utils import create_test_junior_medical_staff


class JuniorMedicalStaffTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def junior_medical_staff_create(self):
        """
        Ensure we can create junior medical staff.
        """
        junior_medical_staff = create_test_junior_medical_staff()
        self.assertTrue(isinstance(junior_medical_staff, JuniorMedicalStaff))
        self.assertEqual(len(JuniorMedicalStaff.objects.all()), 1)
