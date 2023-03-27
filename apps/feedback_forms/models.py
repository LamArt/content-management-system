from django.core.validators import MaxLengthValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField

from apps.common.models import BaseModel


class FeedbackForm(BaseModel):
    name = models.CharField(max_length=256)
    notification_success_template = models.TextField(max_length=1024)
    notification_failure_template = models.TextField(max_length=1024)
    notification_manager_email_template = HTMLField()
    confirmation_email = models.BooleanField(default=False)
    confirmation_email_template = HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"
        ordering = ["id"]


class Field(BaseModel):
    class FieldType(models.TextChoices):
        STRING = "String", "string"
        PHONE = "Phone", "phone"
        EMAIL = "Email", "email"
        FILE = "File", "file"
        HIDDEN = "Hidden", "hidden"

    name = models.CharField(max_length=64)
    marker_template = models.CharField(max_length=64)
    required_field = models.BooleanField()
    type = models.CharField(FieldType, max_length=6, choices=FieldType.choices)
    feedback_forms = models.ManyToManyField(FeedbackForm, related_name="fields")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поле"
        verbose_name_plural = "Поля"
        ordering = ["id"]


class FormEmail(BaseModel):
    email_address = models.EmailField(verbose_name="Адрес электронной почты")
    feedback_forms = models.ManyToManyField(
        FeedbackForm, verbose_name="Формы", related_name="emails", blank=True
    )

    def __str__(self):
        return self.email_address

    class Meta:
        verbose_name = "Почта для форм"
        verbose_name_plural = "Почты для форм"


class FeedbackFormLog(BaseModel):
    datetime = models.DateTimeField(
        auto_created=True, verbose_name="Дата и время заполнения"
    )
    ip_address = models.GenericIPAddressField(verbose_name="IP адрес пользователя")
    url = models.URLField(verbose_name="URL страницы")
    url_source = models.URLField(verbose_name="URL источника посещения")
    name = models.TextField(
        max_length=256, validators=[MaxLengthValidator(256)], verbose_name="Имя"
    )
    phone_number = PhoneNumberField(max_length=17, verbose_name="Телефон")
    email_address = models.EmailField(verbose_name="Email")
    message = models.TextField(
        max_length=2048, validators=[MaxLengthValidator(2048)], verbose_name="Сообщение"
    )
    convenient_time = models.TimeField(verbose_name="Удобное время для связи")
    service_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="Название услуги, из которой отправили заявку",
    )
    page_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="Название страницы, из которой отправили заявку",
    )
    doctor_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="ФИО доктора",
    )
    feedback_form = models.ForeignKey(FeedbackForm, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.datetime)

    class Meta:
        verbose_name = "Запись в журнале"
        verbose_name_plural = "Записи в журнале"
        ordering = ["-datetime"]
