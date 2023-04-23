from django.test import TestCase
from rest_framework.test import APIClient

from apps.ordering.models import TestBaseOrderingModel
from apps.ordering.tests.utils import create_test_ordering_objects


class OrderingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_ordering_objects = [create_test_ordering_objects(i) for i in range(5)]

    @staticmethod
    def get_ordering_values(iterable):
        return list(map(lambda x: x.ordering, iterable))

    @staticmethod
    def get_id_values(iterable):
        return list(map(lambda x: x.id, iterable))

    def test_ordering(self):
        """
        Ensure models were created successfully.
        """
        qs = TestBaseOrderingModel.objects.all()
        self.assertCountEqual(self.test_ordering_objects, qs)
        self.assertListEqual([i for i in range(5)], self.get_ordering_values(qs))
        self.assertListEqual(
            self.get_ordering_values(self.test_ordering_objects),
            self.get_ordering_values(qs),
        )

    def test_delete(self):
        """
        Ensure deletion of model works successfully.
        """
        self.test_ordering_objects[3].delete()
        qs = TestBaseOrderingModel.objects.all()

        self.assertEqual(len(qs), 4)
        self.assertListEqual([1, 2, 3, 5], self.get_id_values(qs))
