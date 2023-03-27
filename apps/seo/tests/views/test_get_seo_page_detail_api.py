from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.seo.tests.utils import create_test_page_seo


class SEODetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_seo_url = lambda pk: reverse("page-detail", args=[pk])

    def test_seo_page_detail_api(self):
        """
        Ensure we can get page seo detail.
        """
        page_seo = create_test_page_seo()
        response = self.client.get(self.get_seo_url(page_seo.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
