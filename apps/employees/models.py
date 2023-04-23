from django.db import models

from apps.images.models import BaseImageModel
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
    class Meta(BaseOrderingModel.Meta):
        verbose_name = "Младший персонал"
        verbose_name_plural = "Младший персонал"


class Administrator(BaseEmployeeModel):
    class Meta(BaseOrderingModel.Meta):
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Director(BaseEmployeeModel):
    class Meta(BaseOrderingModel.Meta):
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"


class EmployeeEducationImage(BaseImageModel):
    class Meta:
        verbose_name = "Образование врача"
        verbose_name_plural = "Образование врача"
        ordering = ["ordering"]


class EmployeeCertificateImage(BaseImageModel):
    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"
        ordering = ["ordering"]


class Employee(PageSEOMixin, BaseEmployeeModel):
    image_patient_photo = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Фотография врача с пациентом",
    )
    video = models.URLField(
        null=True,
        blank=True,
        verbose_name="Видео с представлением врача",
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
        Service, blank=True, related_name="doctors", verbose_name="Услуги"
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
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
        ordering = ["ordering"]
