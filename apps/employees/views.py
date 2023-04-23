from rest_framework import viewsets

from apps.employees.models import (
    JuniorStaff,
    Administrator,
    Director,
    Employee,
    EmployeeEducationImage,
    EmployeeCertificateImage,
)
from apps.employees.serializers import (
    JuniorStaffSerializer,
    AdministratorSerializer,
    DirectorSerializer,
    EmployeeSerializer,
    EmployeeEducationImageSerializer,
    EmployeeCertificateImageSerializer,
)
from apps.seo.utils import PageSEOViewMixin


class JuniorStaffViewSet(viewsets.ModelViewSet):
    basename = "junior-staff"
    queryset = JuniorStaff.objects.all()
    serializer_class = JuniorStaffSerializer
    http_method_names = ["get"]


class AdministratorViewSet(viewsets.ModelViewSet):
    basename = "administrator"
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    http_method_names = ["get"]


class DirectorViewSet(viewsets.ModelViewSet):
    basename = "director"
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    http_method_names = ["get"]


class EmployeeViewSet(PageSEOViewMixin, viewsets.ModelViewSet):
    basename = "employee"
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ["get"]


class EmployeeEducationImageViewSet(viewsets.ModelViewSet):
    basename = "education-image"
    queryset = EmployeeEducationImage.objects.all()
    serializer_class = EmployeeEducationImageSerializer
    http_method_names = ["get"]


class EmployeeCertificateImageViewSet(viewsets.ModelViewSet):
    basename = "certificate-image"
    queryset = EmployeeCertificateImage.objects.all()
    serializer_class = EmployeeCertificateImageSerializer
    http_method_names = ["get"]
