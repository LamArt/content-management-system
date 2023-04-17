from rest_framework import viewsets

from apps.company_description.models import (
    Link,
    Contact,
    ClinicDescription,
    PatientInfo,
    ConstituentDocument,
    Partner,
    ClinicImage,
    StaffImage,
    InformedPatientConsent,
    MedicalProfessionalProvisions,
)
from apps.company_description.api.serializers import (
    LinkSerializer,
    ContactSerializer,
    ClinicDescriptionSerizlier,
    PatientInfoSerializer,
    ConstituentDocumentSerializer,
    PartnerSerializer,
    ClinicImageSerializer,
    StaffImageSerializer,
    InformedPatientConsentSerializer,
    MedicalProfessionalProvisionsSerializer,
)


class LinkViewSet(viewsets.ModelViewSet):
    basename = "link"
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    http_method_names = ["get"]


class ContactViewSet(viewsets.ModelViewSet):
    basename = "contact"
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ["get"]


class ClinicDescriptionViewSet(viewsets.ModelViewSet):
    basename = "clinic-description"
    queryset = ClinicDescription.objects.all()
    serializer_class = ClinicDescriptionSerizlier
    http_method_names = ["get"]


class PatientInfoViewSet(viewsets.ModelViewSet):
    basename = "patient-info"
    queryset = PatientInfo.objects.all()
    serializer_class = PatientInfoSerializer
    http_method_names = ["get"]


class ConstituentDocumentViewSet(viewsets.ModelViewSet):
    basename = "constituent-document"
    queryset = ConstituentDocument.objects.all()
    serializer_class = ConstituentDocumentSerializer
    http_method_names = ["get"]


class InformedPatientConsentViewSet(viewsets.ModelViewSet):
    basename = "informed-patient-consent"
    queryset = InformedPatientConsent.objects.all()
    serializer_class = InformedPatientConsentSerializer
    http_method_names = ["get"]


class MedicalProfessionalProvisionsViewSet(viewsets.ModelViewSet):
    basename = "medical-professional-provisions"
    queryset = MedicalProfessionalProvisions.objects.all()
    serializer_class = MedicalProfessionalProvisionsSerializer
    http_method_names = ["get"]


class PartnerViewSet(viewsets.ModelViewSet):
    basename = "partner"
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    http_method_names = ["get"]


class ClinicImageViewSet(viewsets.ModelViewSet):
    basename = "clinic-image"
    queryset = ClinicImage.objects.all()
    serializer_class = ClinicImageSerializer
    http_method_names = ["get"]


class StaffImageViewSet(viewsets.ModelViewSet):
    basename = "staff-image"
    queryset = StaffImage.objects.all()
    serializer_class = StaffImageSerializer
    http_method_names = ["get"]
