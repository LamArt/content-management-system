from django.db import models
from apps.common.models import BaseModel
from apps.ordering.services import reorder_objects


class BaseOrderingModel(BaseModel):
    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        reorder_objects(type(self))

    class Meta(BaseModel.Meta):
        abstract = True
        ordering = ["ordering"]


class TestBaseOrderingModel(BaseOrderingModel):
    __test__ = False
    pass
