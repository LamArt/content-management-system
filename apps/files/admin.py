from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from apps.ordering.admin import OrderingModelAdmin

data = {
    "list_display": ("name",),
    "fieldsets": (
        (
            "Основное",
            {
                "fields": (  # exclude not fields
                    "name",
                    "path",
                )
            },
        ),
    ),
    "search_fields": ("name",),
}


class BaseFileAdmin(admin.ModelAdmin):
    list_display = tuple()
    fieldsets = tuple()
    search_fields = tuple()

    def __getattribute__(self, name):
        if name in data:
            return data[name] + object.__getattribute__(self, name)
        else:
            return object.__getattribute__(self, name)


class BaseImageAdmin(SortableAdminMixin, OrderingModelAdmin):
    list_display = tuple()
    fieldsets = tuple()
    search_fields = tuple()

    def __getattribute__(self, name):
        if name in data:
            return data[name] + object.__getattribute__(self, name)
        else:
            return object.__getattribute__(self, name)
