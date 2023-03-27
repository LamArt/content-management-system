from django.test import TestCase
from rest_framework.test import APIClient

from apps.company_description.models import StaffImage
from apps.company_description.tests.utils import create_test_staff_image


class StaffImageTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_staff_image_create(self):
        """
        Ensure we can create staff image.
        """
        staff_image = create_test_staff_image()
        self.assertTrue(isinstance(staff_image, StaffImage))
        self.assertEqual(len(StaffImage.objects.all()), 1)
