from rest_framework import serializers

from apps.company_description.models import (
    Contact,
    Link,
    ClinicDescription,
    PatientInfo,
    ConstituentDocument,
    Partner,
    CompanyImage,
    StaffImage,
    InformedPatientConsent,
    MedicalProfessionalProvisions,
)
from apps.files.utils import FileSerializerMixin


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"


class ClinicDescriptionSerizlier(serializers.ModelSerializer):
    class Meta:
        model = ClinicDescription
        fields = "__all__"


class PatientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = "__all__"


class ConstituentDocumentSerializer(FileSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ConstituentDocument
        fields = "__all__"


class InformedPatientConsentSerializer(
    FileSerializerMixin, serializers.ModelSerializer
):
    class Meta:
        model = InformedPatientConsent
        fields = "__all__"


class MedicalProfessionalProvisionsSerializer(
    FileSerializerMixin, serializers.ModelSerializer
):
    class Meta:
        model = MedicalProfessionalProvisions
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class CompanyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImage
        fields = "__all__"


class StaffImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffImage
        fields = "__all__"
