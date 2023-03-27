from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.template.defaultfilters import truncatechars

from apps.common.services import reorder_models
from apps.files.admin import BaseFileAdmin
from apps.seo.utils import PageSEOAdminMixin
from apps.services.models import (
    Service,
    ServiceCategory,
    ServicePatientNeedsCategory,
    ServiceFile,
)


@admin.register(Service)
class ServiceAdmin(PageSEOAdminMixin(prepopulated_slug_field="name"), SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "title",
        "image",
        "price",
        "published",
        "price_published",
        "admin_short_description",
        "admin_long_description",
        "video",
        "service_category",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "name",
                    "code",
                    "title",
                    "image",
                    "price",
                    "published",
                    "price_published",
                    "short_description",
                    "long_description",
                    "video",
                    "service_category",
                    "service_patient_needs_categories",
                    "files",
                )
            },
        ),
    )
    search_fields = (
        "name",
        "title",
        "short_description",
        "long_description",
    )
    list_editable = ("published", "price_published")
    list_filter = ("published", "price_published")
    filter_horizontal = (
        "service_patient_needs_categories",
        "files",
    )

    @admin.display(description="Краткое описание")
    def admin_short_description(self, obj):
        from django.utils.html import strip_tags

        return truncatechars(strip_tags(obj.short_description), 100)

    @admin.display(description="Детальное описание")
    def admin_long_description(self, obj):
        from django.utils.html import strip_tags

        return truncatechars(strip_tags(obj.long_description), 100)

    def delete_queryset(self, *args, **kwargs):
        super().delete_queryset(*args, **kwargs)
        reorder_models(Service)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "logo",
        "admin_short_description",
        "admin_long_description",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "name",
                    "logo",
                    "short_description",
                    "long_description",
                )
            },
        ),
    )
    search_fields = (
        "name",
        "short_description",
        "long_description",
    )

    @admin.display(description="Краткое описание")
    def admin_short_description(self, obj):
        from django.utils.html import strip_tags

        return truncatechars(strip_tags(obj.short_description), 100)

    @admin.display(description="Детальное описание")
    def admin_long_description(self, obj):
        from django.utils.html import strip_tags

        return truncatechars(strip_tags(obj.long_description), 100)


@admin.register(ServicePatientNeedsCategory)
class ServicePatientNeedsCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "logo",
        "admin_short_description",
        "admin_long_description",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "name",
                    "logo",
                    "short_description",
                    "long_description",
                )
            },
        ),
    )
    search_fields = (
        "name",
        "short_description",
        "long_description",
    )

    @admin.display
    def admin_short_description(self, obj):
        return truncatechars(obj.short_description, 100)

    @admin.display
    def admin_long_description(self, obj):
        return truncatechars(obj.long_description, 100)


@admin.register(ServiceFile)
class ServiceFileAdmin(BaseFileAdmin):
    pass
