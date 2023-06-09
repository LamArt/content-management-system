from rest_framework import serializers

from apps.company_description.models import (
    Contact,
    Link,
    CompanyDescription,
    ClientInfo,
    ConstituentDocument,
    Partner,
    CompanyImage,
    StaffImage,
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


class CompanyDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDescription
        fields = "__all__"


class PatientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInfo
        fields = "__all__"


class ConstituentDocumentSerializer(FileSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ConstituentDocument
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
