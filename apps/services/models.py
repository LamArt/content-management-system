from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from tinymce.models import HTMLField

from apps.common.models import BaseModel
from apps.common.services import reorder_models
from apps.files.models import BaseFileModel
from apps.seo.models import PageSEOMixin


class ServiceFile(BaseFileModel):
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        ordering = ["name"]


class ServicePatientNeedsCategory(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Название")
    logo = models.ImageField(
        upload_to="images/%Y/%m/%d/", null=True, blank=True, verbose_name="Пиктограмма"
    )
    short_description = HTMLField(
        default="", null=True, blank=True, verbose_name="Краткое описание"
    )
    long_description = HTMLField(
        default="", null=True, blank=True, verbose_name="Детальное описание"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Потребность пациента"
        verbose_name_plural = "Потребности пациентов"
        ordering = ["name"]


class ServiceCategory(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Название")
    logo = models.ImageField(
        upload_to="images/%Y/%m/%d/", null=True, blank=True, verbose_name="Логотип"
    )
    short_description = HTMLField(
        default="", null=True, blank=True, verbose_name="Краткое описание"
    )
    long_description = HTMLField(
        default="", null=True, blank=True, verbose_name="Детальное описание"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Направление деятельности"
        verbose_name_plural = "Направления деятельности"
        ordering = ["name"]


class Service(PageSEOMixin, BaseModel):
    name = models.CharField(max_length=256, verbose_name="Название")
    code = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="Код услуги"
    )
    title = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="Заголовок"
    )
    image = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Иллюстрирующее изображение",
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal("0.01"))],
        verbose_name="Цена",
    )
    published = models.BooleanField(verbose_name="Опубликовано")
    price_published = models.BooleanField(verbose_name="Публиковать в прайсе")
    short_description = HTMLField(
        default="", null=True, blank=True, verbose_name="Краткое описание"
    )
    long_description = HTMLField(
        default="", null=True, blank=True, verbose_name="Детальное описание"
    )
    video = models.URLField(
        null=True,
        blank=True,
        verbose_name="Видео с представлением услуги",
    )
    service_category = models.ForeignKey(
        ServiceCategory, on_delete=models.PROTECT, verbose_name="Категория"
    )
    service_patient_needs_categories = models.ManyToManyField(
        ServicePatientNeedsCategory, blank=True, verbose_name="Категории потребностей"
    )
    files = models.ManyToManyField(
        ServiceFile, blank=True, verbose_name="Прикрепленные файлы"
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
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["ordering"]
