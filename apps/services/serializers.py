from rest_framework import serializers
from apps.files.utils import FileSerializerMixin
from apps.seo.utils import PageSEOSerializerMixin

from apps.services.models import (
    Service,
    ServiceCategory,
    ServicePatientNeedsCategory,
    ServiceFile,
)


class ServiceSerializer(PageSEOSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"


class ServicePatientNeedsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePatientNeedsCategory
        fields = "__all__"


class ServiceFileSerializer(FileSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ServiceFile
        fields = "__all__"
