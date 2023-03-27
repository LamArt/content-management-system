from django.contrib import admin

from apps.feedback_forms.models import FeedbackFormLog, FormEmail


@admin.register(FeedbackFormLog)
class FeedbackFormLogAdmin(admin.ModelAdmin):
    list_display = (
        "datetime",
        "ip_address",
        "url",
        "url_source",
        "name",
        "phone_number",
        "email_address",
        "message",
        "convenient_time",
        "service_name",
        "page_name",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "datetime",
                    "ip_address",
                    "url",
                    "url_source",
                    "name",
                    "phone_number",
                    "email_address",
                    "message",
                    "convenient_time",
                    "service_name",
                    "page_name",
                )
            },
        ),
    )
    exclude = ("feedback_form",)
    search_fields = (
        "datetime",
        "ip_address",
        "name",
        "phone_number",
        "email_address",
        "message",
        "service_name",
        "page_name",
    )
    readonly_fields = (
        "datetime",
        "ip_address",
        "url",
        "url_source",
        "name",
        "phone_number",
        "email_address",
        "message",
        "convenient_time",
        "service_name",
        "page_name",
    )
    list_filter = (
        "datetime",
        "service_name",
        "page_name",
    )

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(FormEmail)
class FormEmail(admin.ModelAdmin):
    list_display = ("email_address",)
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "email_address",
                    "feedback_forms",
                )
            },
        ),
    )
    filter_horizontal = ("feedback_forms",)
