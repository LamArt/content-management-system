from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.feedback_forms.tests.utils import (
    create_test_feedback_form,
)


class FeedbackFormLogTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post_feedback_form_log_url = reverse("feedback-form-log-list")
        self.feedback_form = create_test_feedback_form()
        self.data = {
            "datetime": "2023-02-24T10:49:38.171Z",
            "ip_address": "127.0.0.1",
            "url": "https://smeg48.ru/",
            "url_source": "https://smeg48.ru/",
            "name": "Ксения",
            "phone_number": "+79222933944",
            "email_address": "admin@example.com",
            "message": "Перезвоните пожалуйста, нужна консультация",
            "convenient_time": "11:45",
            "service_name": "Лечение",
            "page_name": "Услуги",
            "feedback_form": self.feedback_form.id,
        }

    def test_feedback_form_log_api(self):
        """
        Ensure we can post feedback form log.
        """
        response = self.client.post(self.post_feedback_form_log_url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
