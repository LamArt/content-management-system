from django.db import models
from tinymce.models import HTMLField
from solo.models import SingletonModel

from apps.common.models import BaseModel
from apps.common.services import reorder_models
from apps.files.models import BaseFileModel


class Link(BaseModel):
    link_address = models.URLField(verbose_name="Ссылка")
    link_for_messenger = models.BooleanField(default=False, verbose_name="Мессенджер")
    link_for_social_network = models.BooleanField(
        default=False, verbose_name="Социальная сеть"
    )
    logo = models.ImageField(
        upload_to="images/%Y/%m/%d/", null=True, blank=True, verbose_name="Логотип"
    )

    def __str__(self):
        return f"{self.link_address}"

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
        ordering = ["link_address"]


class Contact(SingletonModel):
    address = models.TextField(
        max_length=256, null=True, blank=True, verbose_name="Адрес"
    )
    work_schedule = models.TextField(
        max_length=256, null=True, blank=True, verbose_name="График работы"
    )
    phone_number_cell = models.CharField(
        max_length=64, null=True, blank=True, verbose_name="Мобильный телефон"
    )
    phone_number_home = models.CharField(
        max_length=64, null=True, blank=True, verbose_name="Городской телефон"
    )
    email_address = models.EmailField(null=True, blank=True, verbose_name="Email")
    entance_diagram = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Схема прохода в здание",
    )
    parking_place = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Место для парковки",
    )
    yandex_map = models.TextField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Карта на базе сервиса Яндекс.Карты",
    )
    links = models.ManyToManyField(
        Link, blank=True, related_name="contacts", verbose_name="Ссылки"
    )

    def __str__(self):
        return "Настройки контактов"

    class Meta:
        verbose_name = "Настройки контактов"
        ordering = ["id"]  # SOLVE UnorderedObjectListWarning


class ClinicImage(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Имя изображения")
    path = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        verbose_name="Фотографии из клиники",
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
        verbose_name = "Фотография из клиники"
        verbose_name_plural = "Фотографии из клиники"
        ordering = ["ordering"]


class StaffImage(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Имя изображения")
    path = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        verbose_name="Фотографии с персоналом",
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
        verbose_name = "Фотографии с персоналом"
        verbose_name_plural = "Фотографии с персоналом"
        ordering = ["ordering"]


class ClinicDescription(SingletonModel):
    client_approach_description = models.CharField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name="Описание подхода к пациенту",
    )
    video = models.URLField(
        null=True,
        blank=True,
        verbose_name="Видеоролик с выступлением главного врача клиники",
    )
    clinic_main_doctor_description = models.TextField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name="Описание о главном враче клиники",
    )
    image = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Фото главного врача в клинике",
    )
    clinic_history = models.TextField(
        max_length=2048, null=True, blank=True, verbose_name="История клиники"
    )

    def __str__(self):
        return "Настройки описания клиники"

    class Meta:
        verbose_name = "Настройки описания клиники"
        ordering = ["id"]  # SOLVE UnorderedObjectListWarning


class PatientInfo(SingletonModel):
    typical_contract = models.FileField(
        upload_to="files/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Типичный договор",
    )
    personal_data_policy = HTMLField(
        null=True, blank=True, verbose_name="Политика обработки персональных данных"
    )

    def __str__(self):
        return "Настройки информации для пациентов"

    class Meta:
        verbose_name = "Настройка информации для пациентов"
        ordering = ["id"]  # SOLVE UnorderedObjectListWarning


class ConstituentDocument(BaseFileModel):
    class Meta:
        verbose_name = "Учредительный документ"
        verbose_name_plural = "Учредительные документы"
        ordering = ["name"]


class InformedPatientConsent(BaseFileModel):
    class Meta:
        verbose_name = "Информированное согласие для пациентов"
        verbose_name_plural = "Информированное согласие для пациентов"
        ordering = ["name"]


class MedicalProfessionalProvisions(BaseFileModel):
    class Meta:
        verbose_name = "Положение для медицинских работников"
        verbose_name_plural = "Положения для медицинских работников"
        ordering = ["name"]


class Partner(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Название")
    logo = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Иллюстрирующее изображение",
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    phone_number_cell = models.CharField(
        max_length=64, null=True, blank=True, verbose_name="Мобильный телефон"
    )
    link_address = models.URLField(null=True, blank=True, verbose_name="Сайт партнера")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
        ordering = ["name"]
