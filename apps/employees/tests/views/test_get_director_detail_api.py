from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.employees.tests.utils import create_test_director


class DirectorDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_director_url = lambda pk: reverse("director-detail", args=[pk])

    def test_director_detail_api(self):
        """
        Ensure we can get director detail.
        """
        director = create_test_director()
        response = self.client.get(self.get_director_url(director.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
