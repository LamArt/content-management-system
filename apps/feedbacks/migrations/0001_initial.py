# Generated by Django 4.2.2 on 2023-06-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services", "0001_initial"),
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
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
                ("ordering", models.PositiveIntegerField(default=0)),
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
                ("name", models.CharField(max_length=256, verbose_name="Автор")),
                (
                    "image_avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/%Y/%m/%d/",
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "feedback_text",
                    models.TextField(max_length=1024, verbose_name="Текст отзыва"),
                ),
                (
                    "video",
                    models.URLField(blank=True, null=True, verbose_name="Видеоролик"),
                ),
                (
                    "source_name",
                    models.CharField(
                        blank=True,
                        max_length=256,
                        null=True,
                        verbose_name="Название источника",
                    ),
                ),
                (
                    "source_link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Источник отзыва"
                    ),
                ),
                (
                    "employees",
                    models.ManyToManyField(
                        blank=True, to="employees.employee", verbose_name="Сотрудники"
                    ),
                ),
                (
                    "services",
                    models.ManyToManyField(
                        blank=True, to="services.service", verbose_name="Услуги"
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв клиента",
                "verbose_name_plural": "Отзывы клиентов",
            },
        ),
    ]
