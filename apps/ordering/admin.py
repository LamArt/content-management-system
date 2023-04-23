from django.contrib import admin

# Register your models here.
from apps.ordering.services import reorder_objects


class OrderingModelAdmin(admin.ModelAdmin):
    def delete_queryset(self, *args, **kwargs):
        super().delete_queryset(*args, **kwargs)
        reorder_objects(self.model)
