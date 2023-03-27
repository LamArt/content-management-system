from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class DirectorListApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_directors_url = reverse("director-list")

    def test_director_list_api(self):
        """
        Ensure we can get doctors list.
        """
        response = self.client.get(self.get_directors_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
