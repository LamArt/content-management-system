from django.test import TestCase
from rest_framework.test import APIClient

from apps.feedback_forms.models import FeedbackForm
from apps.feedback_forms.tests.utils import (
    create_test_feedback_form,
    create_test_field,
    create_test_form_email,
)


class FeedbackFormTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.fields = [create_test_field() for i in range(5)]
        self.emails = [create_test_form_email() for i in range(6)]

    def test_feedback_form_create(self):
        """
        Ensure we can create feedback form.
        """
        feedback_form = create_test_feedback_form()
        self.assertTrue(isinstance(feedback_form, FeedbackForm))
        self.assertEqual(len(FeedbackForm.objects.all()), 1)
        feedback_form.fields.set(self.fields)
        feedback_form.emails.set(self.emails)
        self.assertEqual(tuple(feedback_form.fields.all()), tuple(self.fields))
        self.assertEqual(feedback_form.fields.count(), len(self.fields))
        self.assertEqual(tuple(feedback_form.emails.all()), tuple(self.emails))
        self.assertEqual(feedback_form.emails.count(), len(self.emails))
