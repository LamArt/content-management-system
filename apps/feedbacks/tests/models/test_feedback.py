from django.test import TestCase
from rest_framework.test import APIClient

from apps.feedbacks.models import Feedback
from apps.feedbacks.tests.utils import (
    create_test_feedback,
    create_test_service,
    create_test_service_category,
    create_test_employee,
)


class FeedbackTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.service_category = create_test_service_category()
        self.services = [
            create_test_service(service_category=self.service_category, index=i)
            for i in range(5)
        ]
        self.employees = [create_test_employee(i) for i in range(6)]

    def test_feedback_create(self):
        """
        Ensure we can create feedback.
        """
        feedback = create_test_feedback()
        self.assertTrue(isinstance(feedback, Feedback))
        self.assertEqual(len(Feedback.objects.all()), 1)
        feedback.services.set(self.services)
        feedback.employees.set(self.employees)
        self.assertEqual(tuple(feedback.services.all()), tuple(self.services))
        self.assertEqual(feedback.services.count(), len(self.services))
        self.assertEqual(tuple(feedback.employees.all()), tuple(self.employees))
        self.assertEqual(feedback.employees.count(), len(self.employees))
