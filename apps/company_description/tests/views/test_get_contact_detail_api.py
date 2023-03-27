from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_contact


class ContactDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_contact_url = lambda pk: reverse("contact-detail", args=[pk])

    def test_contact_detail_api(self):
        """
        Ensure we can get contact detail.
        """
        contact = create_test_contact()
        response = self.client.get(self.get_contact_url(contact.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
