from django.test import TestCase
from rest_framework.test import APIClient

from apps.contacts.models import Link
from apps.contacts.tests.utils import create_test_link


class LinkTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_link_create(self):
        """
        Ensure we can create link.
        """
        link = create_test_link()
        self.assertTrue(Link.__instancecheck__(link))
        self.assertEqual(len(Link.objects.all()), 1)
