from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.employees.tests.utils import create_test_administrator


class AdministratorDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_administrator_url = lambda pk: reverse(
            "administrator-detail", args=[pk]
        )

    def test_administrator_detail_api(self):
        """
        Ensure we can get administrator detail.
        """
        administrator = create_test_administrator()
        response = self.client.get(self.get_administrator_url(administrator.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
