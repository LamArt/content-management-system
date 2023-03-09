from django.db import models

from apps.common.models import BaseModel


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


class Contact(BaseModel):
    address = models.TextField(max_length=256, verbose_name="Адрес")
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
        return f"{self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["address"]
