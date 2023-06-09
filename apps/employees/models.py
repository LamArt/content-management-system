from django.db import models

from apps.files.models import BaseImageModel
from apps.seo.models import PageSEOMixin
from apps.services.models import Service
from apps.ordering.models import BaseOrderingModel


class BaseEmployeeModel(BaseOrderingModel):
    full_name = models.CharField(max_length=256, verbose_name="ФИО")
    image_photo = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Фотография сотрудника",
    )

    def __str__(self):
        return f"{self.full_name}"

    class Meta(BaseOrderingModel.Meta):
        abstract = True


class JuniorStaff(BaseEmployeeModel):
    class Meta(BaseEmployeeModel.Meta):
        verbose_name = "Младший персонал"
        verbose_name_plural = "Младший персонал"


class Administrator(BaseEmployeeModel):
    class Meta(BaseEmployeeModel.Meta):
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Director(BaseEmployeeModel):
    class Meta(BaseEmployeeModel.Meta):
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"


class EmployeeEducationImage(BaseImageModel):
    class Meta:
        verbose_name = "Образование сотрудника"
        verbose_name_plural = "Образование сотрудника"
        ordering = ["ordering"]


class EmployeeCertificateImage(BaseImageModel):
    class Meta:
        verbose_name = "Сертификат сотрудника"
        verbose_name_plural = "Сертификаты сотрудника"
        ordering = ["ordering"]


class Employee(PageSEOMixin, BaseEmployeeModel):
    image_client_photo = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Фотография клиента с результатом работы",
    )
    video = models.URLField(
        null=True,
        blank=True,
        verbose_name="Видео с представлением сотрудника",
    )
    specialization = models.TextField(
        max_length=256, null=True, blank=True, verbose_name="Специализация"
    )
    skills = models.TextField(
        max_length=1024, null=True, blank=True, verbose_name="Навыки врача"
    )
    start_year = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Стаж работы"
    )
    education_images = models.ManyToManyField(
        EmployeeEducationImage, blank=True, verbose_name="Образование"
    )
    certificate_images = models.ManyToManyField(
        EmployeeCertificateImage, blank=True, verbose_name="Сертификаты"
    )
    services = models.ManyToManyField(
        Service, blank=True, related_name="employees", verbose_name="Услуги"
    )

    class Meta(BaseEmployeeModel.Meta):
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
