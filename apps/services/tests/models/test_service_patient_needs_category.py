from django.test import TestCase
from rest_framework.test import APIClient

from apps.services.models import ServicePatientNeedsCategory
from apps.services.tests.utils import (
    create_test_service_patient_needs_category,
)


class ServicePatientNeedsCategoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_service_patient_needs_category_create(self):
        """
        Ensure we can create service patient needs category.
        """
        service_patient_needs_category = create_test_service_patient_needs_category()
        self.assertTrue(
            isinstance(service_patient_needs_category, ServicePatientNeedsCategory)
        )
        self.assertEqual(len(ServicePatientNeedsCategory.objects.all()), 1)
