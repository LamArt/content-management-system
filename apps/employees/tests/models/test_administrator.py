from django.test import TestCase
from rest_framework.test import APIClient

from apps.employees.models import Administrator
from apps.employees.tests.utils import create_test_administrator


class AdministratorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_administrator_create(self):
        """
        Ensure we can create administrator.
        """
        administrator = create_test_administrator()
        self.assertTrue(isinstance(administrator, Administrator))
        self.assertEqual(len(Administrator.objects.all()), 1)
