from django.test import TestCase
from rest_framework.test import APIClient

from apps.company_description.models import ConstituentDocument
from apps.company_description.tests.utils import create_test_constituent_document


class ConstituentDocumentTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_constituent_document_create(self):
        """
        Ensure we can create constituent document.
        """
        constituent_document = create_test_constituent_document()
        self.assertTrue(isinstance(constituent_document, ConstituentDocument))
        self.assertEqual(len(ConstituentDocument.objects.all()), 1)
