from django.test import TestCase
from rest_framework.test import APIClient

from apps.employees.models import JuniorStaff
from apps.employees.tests.utils import create_test_junior_staff


class JuniorStaffTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def junior_staff_create(self):
        """
        Ensure we can create junior staff.
        """
        junior_staff = create_test_junior_staff()
        self.assertTrue(isinstance(junior_staff, JuniorStaff))
        self.assertEqual(len(JuniorStaff.objects.all()), 1)
