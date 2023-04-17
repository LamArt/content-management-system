from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from apps.common.services import reorder_models
from apps.employees.models import (
    JuniorMedicalStaff,
    Administrator,
    Director,
    EmployeeCertificateImage,
    EmployeeEducationImage,
    Employee,
)
from apps.images.admin import BaseImageAdmin
from apps.seo.utils import PageSEOAdminMixin


# TODO: MAKE IT ABSTRACT
@admin.register(JuniorMedicalStaff)
class JuniorMedicalStaffAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "full_name",
        "image_photo",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "full_name",
                    "image_photo",
                )
            },
        ),
    )
    search_fields = ("full_name",)

    def delete_queryset(self, *args, **kwargs):
        super().delete_queryset(*args, **kwargs)
        reorder_models(JuniorMedicalStaff)


@admin.register(Administrator)
class AdministratorAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "full_name",
        "image_photo",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "full_name",
                    "image_photo",
                )
            },
        ),
    )
    search_fields = ("full_name",)

    def delete_queryset(self, *args, **kwargs):
        super().delete_queryset(*args, **kwargs)
        reorder_models(JuniorMedicalStaff)


@admin.register(Director)
class DirectorAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "full_name",
        "image_photo",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "full_name",
                    "image_photo",
                )
            },
        ),
    )
    search_fields = ("full_name",)

    def delete_queryset(self, *args, **kwargs):
        super().delete_queryset(*args, **kwargs)
        reorder_models(JuniorMedicalStaff)


@admin.register(Employee)
class EmployeeAdmin(
    PageSEOAdminMixin("full_name"), SortableAdminMixin, admin.ModelAdmin
):
    list_display = (
        "full_name",
        "image_photo",
        "image_patient_photo",
        "video",
        "specialization",
        "skills",
        "start_year",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "full_name",
                    "image_photo",
                    "image_patient_photo",
                    "video",
                    "specialization",
                    "skills",
                    "start_year",
                    "education_images",
                    "certificate_images",
                    "services",
                )
            },
        ),
    )
    search_fields = (
        "full_name",
        "specialization",
        "skills",
    )
    list_filter = (
        "specialization",
        "skills",
    )
    filter_horizontal = (
        "education_images",
        "certificate_images",
        "services",
    )

    def delete_queryset(self, *args, **kwargs):
        super().delete_queryset(*args, **kwargs)
        reorder_models(Employee)


@admin.register(EmployeeCertificateImage)
class EmployeeCertificateImageAdmin(BaseImageAdmin):
    pass


@admin.register(EmployeeEducationImage)
class DoctorEducationAdmin(BaseImageAdmin):
    pass
