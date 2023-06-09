from django.db import models

from apps.common.models import BaseModel
from apps.ordering.models import BaseOrderingModel


class BaseFileModel(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Имя файла")
    path = models.FileField(upload_to="files/%Y/%m/%d/", verbose_name="Файл")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = True


class BaseImageModel(BaseOrderingModel):
    name = models.CharField(max_length=256, verbose_name="Имя изображения")
    path = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        verbose_name="Изображение",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta(BaseOrderingModel.Meta):
        abstract = True
