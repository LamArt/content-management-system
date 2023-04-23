from django.urls import include, path
from rest_framework import routers

from apps.employees.views import (
    JuniorStaffViewSet,
    AdministratorViewSet,
    DirectorViewSet,
    EmployeeViewSet,
    EmployeeEducationImageViewSet,
    EmployeeCertificateImageViewSet,
)

router = routers.DefaultRouter()
router.register(
    r"junior-staff",
    JuniorStaffViewSet,
    basename=JuniorStaffViewSet.basename,
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
