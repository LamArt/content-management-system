from django.contrib import admin

from apps.seo.models import PageSEO
from apps.seo.utils import PageSEOAdminMixin


@admin.register(PageSEO)
class SEOTagAdmin(PageSEOAdminMixin(), admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": ("id", "name"),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if r"/admin/seo/pageseo/add/" != request.path:
            return ["id"]
        return []

    search_fields = (
        "name",
        "id",
    )
