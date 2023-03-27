from django.test import TestCase
from rest_framework.test import APIClient
from apps.seo.models import PageSEO
from apps.seo.tests.utils import create_test_page_seo


class SEOTagTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_page_seo_create(self):
        """
        Ensure we can create page seo.
        """
        page_seo = create_test_page_seo()
        self.assertTrue(isinstance(page_seo, PageSEO))
        self.assertEqual(len(PageSEO.objects.all()), 1)
