from django.test import TestCase
from rest_framework.test import APIClient

from apps.services.models import ServiceFile
from apps.services.tests.utils import create_test_service_file


class FileTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_service_file_create(self):
        """
        Ensure we can create service file.
        """
        service_file = create_test_service_file()
        self.assertTrue(isinstance(service_file, ServiceFile))
        self.assertEqual(len(ServiceFile.objects.all()), 1)
