from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.feedback_forms.tests.utils import create_test_feedback_form


class FeedbackFormDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_feedback_form_url = lambda pk: reverse(
            "feedback-form-detail", args=[pk]
        )
        self.get_feedback_form_fields_url = lambda pk: reverse(
            "feedback-form-fields", args=[pk]
        )

    def test_feedback_form_detail_api(self):
        """
        Ensure we can get feedback form detail.
        """
        feedback_form = create_test_feedback_form()
        response = self.client.get(self.get_feedback_form_url(feedback_form.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_with_fields = self.client.get(
            self.get_feedback_form_fields_url(feedback_form.id)
        )
        self.assertEqual(response_with_fields.status_code, status.HTTP_200_OK)
