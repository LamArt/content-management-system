from django.db import models

from apps.common.models import BaseModel


class BaseFileModel(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Имя файла")
    path = models.FileField(upload_to="files/%Y/%m/%d/", verbose_name="Файл")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = True
