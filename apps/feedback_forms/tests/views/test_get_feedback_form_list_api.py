from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class FeedbackFormListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_feedback_form_url = reverse("feedback-form-list")

    def test_feedback_form_detail_api(self):
        """
        Ensure we can get feedback form detail.
        """
        response = self.client.get(self.get_feedback_form_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
