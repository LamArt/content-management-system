from django.test import TestCase
from rest_framework.test import APIClient

from apps.services.models import Service
from apps.services.tests.utils import (
    create_test_service,
    create_test_service_category,
    create_test_service_patient_needs_category,
    create_test_service_file,
    create_test_doctor,
)


class ServiceTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.service_category = create_test_service_category()
        self.service_patient_needs_categories = [
            create_test_service_patient_needs_category() for i in range(5)
        ]
        self.files = [create_test_service_file() for i in range(6)]
        self.doctors = [create_test_doctor(i) for i in range(8)]

    def test_service_create(self):
        """
        Ensure we can create service.
        """
        service = create_test_service(service_category=self.service_category)
        self.assertTrue(isinstance(service, Service))
        self.assertEqual(len(Service.objects.all()), 1)
        service.service_patient_needs_categories.set(
            self.service_patient_needs_categories
        )
        service.files.set(self.files)
        service.doctors.set(self.doctors)
        self.assertEqual(
            tuple(service.service_patient_needs_categories.all()),
            tuple(self.service_patient_needs_categories),
        )
        self.assertEqual(
            service.service_patient_needs_categories.count(),
            len(self.service_patient_needs_categories),
        )
        self.assertEqual(tuple(service.files.all()), tuple(self.files))
        self.assertEqual(service.files.count(), len(self.files))
        self.assertEqual(tuple(service.doctors.all()), tuple(self.doctors))
        self.assertEqual(service.doctors.count(), len(self.doctors))
