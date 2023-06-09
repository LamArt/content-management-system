from django.db import models

from apps.ordering.models import BaseOrderingModel
from apps.employees.models import Employee
from apps.seo.models import PageSEOMixin
from apps.services.models import Service


class Portfolio(PageSEOMixin, BaseOrderingModel):
    task_description = models.TextField(max_length=1024, verbose_name="Задача")
    problem_solve = models.TextField(
        max_length=4096, null=True, blank=True, verbose_name="Решение"
    )
    client_result = models.TextField(
        max_length=4096, null=True, blank=True, verbose_name="Результат для клиента"
    )
    image_avatar = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Фото клиента",
    )
    video = models.URLField(null=True, blank=True, verbose_name="Видео")
    completion_date_result = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="Срок достижения результата"
    )
    services = models.ManyToManyField(
        Service, blank=True, related_name="portfolios", verbose_name="Услуги"
    )
    employees = models.ManyToManyField(
        Employee, blank=True, related_name="portfolios", verbose_name="Сотрудники"
    )

    def __str__(self):
        return f"{self.task_description}"

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"
