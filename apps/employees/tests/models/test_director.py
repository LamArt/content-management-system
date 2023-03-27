from django.test import TestCase
from rest_framework.test import APIClient

from apps.employees.models import Director
from apps.employees.tests.utils import create_test_director


class DirectorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_director_create(self):
        """
        Ensure we can create director.
        """
        director = create_test_director()
        self.assertTrue(isinstance(director, Director))
        self.assertEqual(len(Director.objects.all()), 1)
