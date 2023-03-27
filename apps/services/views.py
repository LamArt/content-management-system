from rest_framework import viewsets

from apps.seo.utils import PageSEOViewMixin
from apps.services.models import (
    Service,
    ServiceCategory,
    ServicePatientNeedsCategory,
    ServiceFile,
)
from apps.services.serializers import (
    ServiceSerializer,
    ServiceCategorySerializer,
    ServicePatientNeedsCategorySerializer,
    ServiceFileSerializer,
)


class ServiceViewSet(PageSEOViewMixin, viewsets.ModelViewSet):
    basename = "service"
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    http_method_names = ["get"]


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    basename = "service-category"
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    http_method_names = ["get"]


class ServicePatientNeedsCategoryViewSet(viewsets.ModelViewSet):
    basename = "patient-category"
    queryset = ServicePatientNeedsCategory.objects.all()
    serializer_class = ServicePatientNeedsCategorySerializer
    http_method_names = ["get"]


class FileViewSet(viewsets.ModelViewSet):
    basename = "service-file"
    queryset = ServiceFile.objects.all()
    serializer_class = ServiceFileSerializer
    http_method_names = ["get"]
