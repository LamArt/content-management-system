# Generated by Django 4.2.2 on 2023-06-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PageSEO",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Время изменения"),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        max_length=256,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                (
                    "meta_title",
                    models.TextField(
                        blank=True,
                        default="",
                        max_length=256,
                        null=True,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "meta_keywords",
                    models.TextField(
                        blank=True,
                        default="",
                        max_length=256,
                        null=True,
                        verbose_name="Ключевые слова",
                    ),
                ),
                (
                    "meta_description",
                    models.TextField(
                        blank=True,
                        default="",
                        max_length=256,
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=128,
                        null=True,
                        verbose_name="Имя страницы",
                    ),
                ),
            ],
            options={
                "verbose_name": "SEO-тэги страницы",
                "verbose_name_plural": "SEO-тэги страниц",
                "ordering": ["name"],
            },
        ),
    ]
