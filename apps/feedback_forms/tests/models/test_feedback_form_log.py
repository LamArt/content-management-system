from django.test import TestCase
from rest_framework.test import APIClient

from apps.feedback_forms.models import FeedbackFormLog
from apps.feedback_forms.tests.utils import (
    create_test_feedback_form_log,
    create_test_feedback_form,
)


class FeedbackFormLogTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.feedback_form = create_test_feedback_form()

    def test_feedback_form_log_create(self):
        """
        Ensure we can create feedback form log.
        """
        feedback_form_log = create_test_feedback_form_log(self.feedback_form)
        self.assertTrue(isinstance(feedback_form_log, FeedbackFormLog))
        self.assertEqual(len(FeedbackFormLog.objects.all()), 1)
