from django.contrib import admin

from apps.contacts.models import Contact, Link


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
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
class LinkAdmin(admin.ModelAdmin):
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
