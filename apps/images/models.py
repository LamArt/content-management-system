from django.db import models

from apps.common.models import BaseModel
from apps.common.services import reorder_models


class BaseImageModel(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Имя изображения")
    path = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        verbose_name="Изображение",
    )

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        reorder_models(type(self))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = True
