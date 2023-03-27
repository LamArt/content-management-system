from django.test import TestCase
from rest_framework.test import APIClient
from django.db.utils import IntegrityError

from apps.company_description.models import Contact
from apps.company_description.tests.utils import create_test_link, create_test_contact


class ContactTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.links = [create_test_link() for i in range(5)]

    def test_contact_create(self):
        """
        Ensure we can create contact. Provide singleton model.
        """
        contact = create_test_contact()
        contact.links.add(*[link for link in self.links])
        self.assertTrue(isinstance(contact, Contact))
        self.assertEqual(len(Contact.objects.all()), 1)
        self.assertEqual(tuple(contact.links.all()), tuple(self.links))
        self.assertEqual(contact.links.count(), len(self.links))
        self.assertRaises(IntegrityError, create_test_contact)
