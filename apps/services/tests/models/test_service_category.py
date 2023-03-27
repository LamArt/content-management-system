from django.test import TestCase
from rest_framework.test import APIClient

from apps.services.models import ServiceCategory
from apps.services.tests.utils import create_test_service_category


class ServiceCategoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_service_category_create(self):
        """
        Ensure we can create service category.
        """
        service_category = create_test_service_category()
        self.assertTrue(isinstance(service_category, ServiceCategory))
        self.assertEqual(len(ServiceCategory.objects.all()), 1)
