from django.db import models

from apps.common.models import BaseModel
from apps.employees.models import Employee
from apps.services.models import Service


class Feedback(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Автор")
    image_avatar = models.ImageField(
        upload_to="images/%Y/%m/%d/", null=True, blank=True, verbose_name="Аватар"
    )
    feedback_text = models.TextField(max_length=1024, verbose_name="Текст отзыва")
    video = models.URLField(null=True, blank=True, verbose_name="Видеоролик")
    source_name = models.CharField(
        max_length=256, null=True, blank=True, verbose_name="Название источника"
    )
    source_link = models.URLField(null=True, blank=True, verbose_name="Источник отзыва")
    doctors = models.ManyToManyField(Employee, blank=True, verbose_name="Доктора")
    services = models.ManyToManyField(Service, blank=True, verbose_name="Услуги")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Отзыв пациента"
        verbose_name_plural = "Отзывы пациентов"
        ordering = ["name"]
