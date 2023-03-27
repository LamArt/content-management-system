from django.test import TestCase
from rest_framework.test import APIClient

from apps.feedback_forms.models import Field
from apps.feedback_forms.tests.utils import create_test_field


class FieldTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_field_create(self):
        """
        Ensure we can create field.
        """
        field = create_test_field()
        self.assertTrue(isinstance(field, Field))
        self.assertEqual(len(Field.objects.all()), 1)
