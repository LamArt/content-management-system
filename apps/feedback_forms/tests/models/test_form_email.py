from django.test import TestCase
from rest_framework.test import APIClient

from apps.feedback_forms.models import FormEmail
from apps.feedback_forms.tests.utils import create_test_form_email


class FormEmailTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_form_email_create(self):
        """
        Ensure we can create form email.
        """
        form_email = create_test_form_email()
        self.assertTrue(isinstance(form_email, FormEmail))
        self.assertEqual(len(FormEmail.objects.all()), 1)
