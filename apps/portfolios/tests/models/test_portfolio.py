from django.test import TestCase
from rest_framework.test import APIClient

from apps.portfolios.models import Portfolio
from apps.portfolios.tests.utils import (
    create_test_portfolio,
    create_test_employee,
    create_test_service_category,
    create_test_service,
)


class PortfolioTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.service_category = create_test_service_category()
        self.services = [
            create_test_service(service_category=self.service_category, index=i)
            for i in range(5)
        ]
        self.employees = [create_test_employee(i) for i in range(6)]

    def test_portfolio_create(self):
        """
        Ensure we can create portfolio.
        """
        portfolio = create_test_portfolio()
        self.assertTrue(isinstance(portfolio, Portfolio))
        self.assertEqual(len(Portfolio.objects.all()), 1)
        portfolio.services.set(self.services)
        portfolio.employees.set(self.employees)
        self.assertEqual(tuple(portfolio.services.all()), tuple(self.services))
        self.assertEqual(portfolio.services.count(), len(self.services))
        self.assertEqual(tuple(portfolio.employees.all()), tuple(self.employees))
        self.assertEqual(portfolio.employees.count(), len(self.employees))
