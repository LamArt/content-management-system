from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.feedbacks.tests.utils import create_test_feedback


class FeedbackDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_feedback_url = lambda pk: reverse("feedback-detail", args=[pk])

    def test_feedback_detail_api(self):
        """
        Ensure we can get feedback detail.
        """
        feedback = create_test_feedback()
        response = self.client.get(self.get_feedback_url(feedback.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
