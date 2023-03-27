from django.urls import include, path
from rest_framework import routers

from apps.employees.views import (
    JuniorMedicalStaffViewSet,
    AdministratorViewSet,
    DirectorViewSet,
    EmployeeViewSet,
    EmployeeEducationImageViewSet,
    EmployeeCertificateImageViewSet,
)

router = routers.DefaultRouter()
router.register(
    r"junior-medical-staff",
    JuniorMedicalStaffViewSet,
    basename=JuniorMedicalStaffViewSet.basename,
)
router.register(
    r"administrator", AdministratorViewSet, basename=AdministratorViewSet.basename
)
router.register(r"director", DirectorViewSet, basename=DirectorViewSet.basename)

router.register(r"employee", EmployeeViewSet, basename=EmployeeViewSet.basename)
router.register(
    r"education-image",
    EmployeeEducationImageViewSet,
    basename=EmployeeEducationImageViewSet.basename,
)
router.register(
    r"certificate-image",
    EmployeeCertificateImageViewSet,
    basename=EmployeeCertificateImageViewSet.basename,
)


urlpatterns = [
    path("", include(router.urls)),
]
