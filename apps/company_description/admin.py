from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from solo.admin import SingletonModelAdmin

from apps.company_description.models import (
    Contact,
    Link,
    CompanyImage,
    StaffImage,
    ClinicDescription,
    PatientInfo,
    ConstituentDocument,
    InformedPatientConsent,
    MedicalProfessionalProvisions,
    Partner,
)
from apps.common.services import reorder_models
from apps.files.admin import BaseFileAdmin
from apps.ordering.admin import OrderingModelAdmin


@admin.register(Contact)
class ContactAdmin(SingletonModelAdmin):
    list_display = (
        "address",
        "work_schedule",
        "phone_number_cell",
        "phone_number_home",
        "email_address",
        "entance_diagram",
        "parking_place",
        "yandex_map",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "address",
                    "work_schedule",
                    "phone_number_cell",
                    "phone_number_home",
                    "email_address",
                    "entance_diagram",
                    "parking_place",
                    "yandex_map",
                    "links",
                )
            },
        ),
    )
    search_fields = (
        "address",
        "work_schedule",
        "phone_number_cell",
        "phone_number_home",
        "email_address",
    )
    filter_horizontal = ("links",)


@admin.register(Link)
class LinkAdmin(SortableAdminMixin, OrderingModelAdmin):
    list_display = (
        "link_address",
        "link_for_messenger",
        "link_for_social_network",
        "logo",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "link_address",
                    "link_for_messenger",
                    "link_for_social_network",
                    "logo",
                )
            },
        ),
    )
    list_editable = (
        "link_for_messenger",
        "link_for_social_network",
    )
    list_filter = (
        "link_for_messenger",
        "link_for_social_network",
    )


@admin.register(CompanyImage)
class CompanyImageAdmin(SortableAdminMixin, OrderingModelAdmin):
    list_display = ("name",)
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "name",
                    "path",
                )
            },
        ),
    )
    search_fields = ("name",)


@admin.register(StaffImage)
class StaffImageAdmin(SortableAdminMixin, OrderingModelAdmin):
    list_display = ("name",)
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "name",
                    "path",
                )
            },
        ),
    )
    search_fields = ("name",)


@admin.register(ClinicDescription)
class ClinicDescriptionAdmin(SingletonModelAdmin):
    list_display = (
        "client_approach_description",
        "video",
        "clinic_main_doctor_description",
        "image",
        "clinic_history",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "client_approach_description",
                    "video",
                    "clinic_main_doctor_description",
                    "image",
                    "clinic_history",
                )
            },
        ),
    )


@admin.register(PatientInfo)
class PatientInfoAdmin(SingletonModelAdmin):
    list_display = (
        "typical_contract",
        "personal_data_policy",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "typical_contract",
                    "personal_data_policy",
                )
            },
        ),
    )


@admin.register(ConstituentDocument)
class ConstituentDocumentAdmin(BaseFileAdmin):
    pass


@admin.register(InformedPatientConsent)
class InformedPatientConsentAdmin(BaseFileAdmin):
    pass


@admin.register(MedicalProfessionalProvisions)
class MedicalProfessionalProvisionsAdmin(BaseFileAdmin):
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "logo",
        "description",
        "phone_number_cell",
        "link_address",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "name",
                    "logo",
                    "description",
                    "phone_number_cell",
                    "link_address",
                )
            },
        ),
    )
    search_fields = (
        "name",
        "description",
        "phone_number_cell",
        "link_address",
    )
