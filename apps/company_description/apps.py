from django.apps import AppConfig


class CompanyDescriptionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.company_description"
    verbose_name = "Управление информацией о компании"
