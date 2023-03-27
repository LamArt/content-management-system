from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.company_description.tests.utils import create_test_constituent_document


class ConstituentDocumentDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_constituent_document_url = lambda pk: reverse(
            "constituent-document-detail", args=[pk]
        )

    def test_constituent_document_detail_api(self):
        """
        Ensure we can get constituent document detail.
        """
        constituent_document = create_test_constituent_document()
        response = self.client.get(
            self.get_constituent_document_url(constituent_document.id)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
