from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class FeedbackListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_feedback_url = reverse("feedback-list")

    def test_feedback_list_api(self):
        """
        Ensure we can get feedback list.
        """
        response = self.client.get(self.get_feedback_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
