from django.db import models

from apps.common.models import BaseModel
from apps.employees.models import Employee
from apps.seo.models import PageSEOMixin
from apps.services.models import Service


class Portfolio(PageSEOMixin, BaseModel):
    task_description = models.TextField(max_length=1024, verbose_name="Задача")
    problem_solve = models.TextField(
        max_length=4096, null=True, blank=True, verbose_name="Решение"
    )
    patient_result = models.TextField(
        max_length=4096, null=True, blank=True, verbose_name="Результат для пациента"
    )
    image_avatar = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Фото пациента",
    )
    video = models.URLField(null=True, blank=True, verbose_name="Видео")
    completion_date_result = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="Срок достижения результата"
    )
    services = models.ManyToManyField(
        Service, blank=True, related_name="portfolios", verbose_name="Услуги"
    )
    doctors = models.ManyToManyField(
        Employee, blank=True, related_name="portfolios", verbose_name="Врачи"
    )

    def __str__(self):
        return f"{self.task_description}"

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"
        ordering = ["task_description"]
