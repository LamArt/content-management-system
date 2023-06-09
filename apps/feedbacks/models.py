from django.db import models
from django.db.models import signals
from django.dispatch import receiver

from apps.employees.models import Employee
from apps.ordering.models import BaseOrderingModel
from apps.seo.models import PageSEOMixin
from apps.services.models import Service


class Feedback(PageSEOMixin, BaseOrderingModel):
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
    employees = models.ManyToManyField(Employee, blank=True, verbose_name="Сотрудники")
    services = models.ManyToManyField(Service, blank=True, verbose_name="Услуги")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Отзыв клиента"
        verbose_name_plural = "Отзывы клиентов"


@receiver(signals.pre_save, sender=Feedback)
def before_create_feedback(sender, instance, **kwargs):
    if not instance.pk:
        feedbacks = sender.objects.order_by("ordering").all()
        for i, feedback in enumerate(feedbacks, 2):
            feedback.ordering = i
            feedback.save(update_fields=["ordering"])


@receiver(signals.post_save, sender=Feedback)
def after_create_feedback(sender, instance, created, **kwargs):
    if created:
        instance.ordering = 1
        instance.save()
