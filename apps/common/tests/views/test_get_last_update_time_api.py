from django.urls import reverse
from django.test import TestCase
from django.utils.dateparse import parse_datetime
from rest_framework import status
from rest_framework.test import APIClient

import ast

from apps.common.tests.utils import create_test_contact


class LastUpdateTimeApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_last_update_time_url = reverse("last-update-time")
        self.example_instance = create_test_contact()

    def test_get_last_update_time_api(self):
        """
        Ensure we can get last update time.
        """
        response = self.client.get(self.get_last_update_time_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            parse_datetime(
                ast.literal_eval(response.content.decode("utf-8"))["last_update_time"]
            ).strftime("%Y-%m-%d %H:%M:%S"),
            self.example_instance.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        )
        self.assertEqual(
            parse_datetime(
                ast.literal_eval(response.content.decode("utf-8"))["last_update_time"]
            ).strftime("%Y-%m-%d %H:%M:%S"),
            self.example_instance.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        )
