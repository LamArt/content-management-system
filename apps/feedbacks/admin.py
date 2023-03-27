from django.contrib import admin

from apps.feedbacks.models import Feedback


@admin.register(Feedback)
class ServiceFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "image_avatar",
        "feedback_text",
        "video",
        "source_name",
        "source_link",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "name",
                    "image_avatar",
                    "feedback_text",
                    "video",
                    "source_name",
                    "source_link",
                    "services",
                    "doctors",
                )
            },
        ),
    )
    search_fields = (
        "name",
        "feedback_text",
        "source_name",
    )
    list_filter = (
        "name",
        "source_name",
        "services",
        "doctors",
    )
    filter_horizontal = (
        "services",
        "doctors",
    )
