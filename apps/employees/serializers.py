from rest_framework.serializers import ModelSerializer

from apps.employees.models import (
    JuniorMedicalStaff,
    Administrator,
    Director,
    Employee,
    EmployeeEducationImage,
    EmployeeCertificateImage,
)
from apps.seo.utils import PageSEOSerializerMixin


class JuniorMedicalStaffSerializer(ModelSerializer):
    class Meta:
        model = JuniorMedicalStaff
        fields = "__all__"


class AdministratorSerializer(ModelSerializer):
    class Meta:
        model = Administrator
        fields = "__all__"


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class EmployeeSerializer(PageSEOSerializerMixin, ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeEducationImageSerializer(ModelSerializer):
    class Meta:
        model = EmployeeEducationImage
        fields = "__all__"


class EmployeeCertificateImageSerializer(ModelSerializer):
    class Meta:
        model = EmployeeCertificateImage
        fields = "__all__"
