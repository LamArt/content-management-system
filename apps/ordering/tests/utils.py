from apps.ordering.models import TestBaseOrderingModel


def create_test_ordering_objects(i):
    item = TestBaseOrderingModel.objects.create()
    item.ordering = i
    item.save()
    return item
