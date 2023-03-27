from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_link


class LinkDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_contact_url = lambda pk: reverse("link-detail", args=[pk])

    def test_contact_detail_api(self):
        """
        Ensure we can get contact detail.
        """
        link = create_test_link()
        response = self.client.get(self.get_contact_url(link.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
