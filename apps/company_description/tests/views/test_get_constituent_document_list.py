from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ConstituentDocumentApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_constituent_documents_url = reverse("constituent-document-list")

    def test_constituent_documents_list_api(self):
        """
        Ensure we can get constituent documents list.
        """
        response = self.client.get(self.get_constituent_documents_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
