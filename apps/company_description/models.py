from django.db import models
from tinymce.models import HTMLField
from solo.models import SingletonModel

from apps.common.models import BaseModel
from apps.ordering.models import BaseOrderingModel
from apps.files.models import BaseFileModel, BaseImageModel


class Link(BaseOrderingModel):
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

    class Meta(BaseOrderingModel.Meta):
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"


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


class CompanyImage(BaseImageModel):
    class Meta(BaseImageModel.Meta):
        verbose_name = "Фотография из офиса компании"
        verbose_name_plural = "Фотографии из офиса компании"


class StaffImage(BaseImageModel):
    class Meta(BaseImageModel.Meta):
        verbose_name = "Фотографии с персоналом"
        verbose_name_plural = "Фотографии с персоналом"


class CompanyDescription(SingletonModel):
    client_approach_description = models.CharField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name="Описание подхода к клиенту",
    )
    video = models.URLField(
        null=True,
        blank=True,
        verbose_name="Видеоролик с выступлением директора компании",
    )
    company_main_director_description = models.TextField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name="Описание директора компании",
    )
    image = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Фото директора в компании",
    )
    company_history = models.TextField(
        max_length=2048, null=True, blank=True, verbose_name="История компании"
    )

    def __str__(self):
        return "Настройки описания компании"

    class Meta:
        verbose_name = "Настройки описания клиники"


class ClientInfo(SingletonModel):
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


class ConstituentDocument(BaseFileModel):
    class Meta:
        verbose_name = "Учредительный документ"
        verbose_name_plural = "Учредительные документы"
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
