from django.contrib import admin

from apps.portfolios.models import Portfolio
from apps.seo.utils import PageSEOAdminMixin


@admin.register(Portfolio)
class PortfolioAdmin(PageSEOAdminMixin("task_description"), admin.ModelAdmin):
    list_display = (
        "task_description",
        "problem_solve",
        "patient_result",
        "image_avatar",
        "video",
        "completion_date_result",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "task_description",
                    "problem_solve",
                    "patient_result",
                    "image_avatar",
                    "video",
                    "completion_date_result",
                    "services",
                    "doctors",
                )
            },
        ),
    )
    search_fields = (
        "task_description",
        "problem_solve",
        "patient_result",
        "completion_date_result",
    )
    filter_horizontal = (
        "services",
        "doctors",
    )
