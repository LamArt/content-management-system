from django.db import models

from apps.common.models import BaseModel


class PageSEOMixin(models.Model):
    slug = models.SlugField(
        max_length=256,
        unique=True,
        allow_unicode=True,
        db_index=True,
        verbose_name="URL",
    )
    meta_title = models.TextField(
        max_length=256, null=True, blank=True, default=str(), verbose_name="Заголовок"
    )
    meta_keywords = models.TextField(
        max_length=256,
        null=True,
        blank=True,
        default=str(),
        verbose_name="Ключевые слова",
    )
    meta_description = models.TextField(
        max_length=256, null=True, blank=True, default=str(), verbose_name="Описание"
    )

    class Meta:
        abstract = True


class PageSEO(BaseModel, PageSEOMixin):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        default=str(),
        verbose_name="Имя страницы",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "SEO-тэги страницы"
        verbose_name_plural = "SEO-тэги страниц"
        ordering = ["name"]
