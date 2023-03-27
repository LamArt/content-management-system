from django.urls import path, include
from apps.services.views import (
    ServiceViewSet,
    ServiceCategoryViewSet,
    ServicePatientNeedsCategoryViewSet,
    FileViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"service", ServiceViewSet, basename=ServiceViewSet.basename)
router.register(
    r"service-category",
    ServiceCategoryViewSet,
    basename=ServiceCategoryViewSet.basename,
)
router.register(
    r"patient-category",
    ServicePatientNeedsCategoryViewSet,
    basename=ServicePatientNeedsCategoryViewSet.basename,
)
router.register(r"service-file", FileViewSet, basename=FileViewSet.basename)

urlpatterns = [
    path("", include(router.urls)),
]
