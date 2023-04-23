from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from apps.common.services import reorder_models
from apps.employees.models import (
    JuniorStaff,
    Administrator,
    Director,
    EmployeeCertificateImage,
    EmployeeEducationImage,
    Employee,
)
from apps.images.admin import BaseImageAdmin
from apps.seo.utils import PageSEOAdminMixin
from apps.ordering.admin import OrderingModelAdmin


# TODO: MAKE IT ABSTRACT
@admin.register(JuniorStaff)
class JuniorStaffAdmin(SortableAdminMixin, OrderingModelAdmin):
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


@admin.register(Administrator)
class AdministratorAdmin(SortableAdminMixin, OrderingModelAdmin):
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


@admin.register(Director)
class DirectorAdmin(SortableAdminMixin, OrderingModelAdmin):
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


@admin.register(Employee)
class EmployeeAdmin(
    PageSEOAdminMixin("full_name"), SortableAdminMixin, OrderingModelAdmin
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


@admin.register(EmployeeCertificateImage)
class EmployeeCertificateImageAdmin(BaseImageAdmin):
    pass


@admin.register(EmployeeEducationImage)
class DoctorEducationAdmin(BaseImageAdmin):
    pass
