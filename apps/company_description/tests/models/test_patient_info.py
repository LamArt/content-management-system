from django.test import TestCase
from django.db.utils import IntegrityError
from rest_framework.test import APIClient

from apps.company_description.models import ClientInfo
from apps.company_description.tests.utils import create_test_patient_info


class PatientInfoTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_patient_info_create(self):
        """
        Ensure we can create patient info. Provide singleton model
        """
        patient_info = create_test_patient_info()
        self.assertTrue(isinstance(patient_info, ClientInfo))
        self.assertEqual(len(ClientInfo.objects.all()), 1)
        self.assertRaises(IntegrityError, create_test_patient_info)
