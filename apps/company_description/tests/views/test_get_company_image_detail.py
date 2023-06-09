from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_company_image


class CompanyImageDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_company_image_url = lambda pk: reverse(
            "company-image-detail", args=[pk]
        )

    def test_company_image_detail_api(self):
        """
        Ensure we can get company image detail.
        """
        company_image = create_test_company_image()
        response = self.client.get(self.get_company_image_url(company_image.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
