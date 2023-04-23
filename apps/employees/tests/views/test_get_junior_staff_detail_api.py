from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.employees.tests.utils import create_test_junior_staff


class JuniorStaffDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_junior_staff_url = lambda pk: reverse(
            "junior-staff-detail", args=[pk]
        )

    def test_junior_staff_detail_api(self):
        """
        Ensure we can get junior staff detail.
        """
        junior_staff = create_test_junior_staff()
        response = self.client.get(
            self.get_junior_staff_url(junior_staff.id)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
