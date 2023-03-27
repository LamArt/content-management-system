from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.portfolios.tests.utils import create_test_portfolio


class PortfolioDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_portfolio_url = lambda pk: reverse("portfolio-detail", args=[pk])

    def test_portfolio_detail_api(self):
        """
        Ensure we can get portfolio detail.
        """
        portfolio = create_test_portfolio()
        response = self.client.get(self.get_portfolio_url(portfolio.slug))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
