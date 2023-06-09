from rest_framework import viewsets

from apps.company_description.models import (
    Link,
    Contact,
    CompanyDescription,
    ClientInfo,
    ConstituentDocument,
    Partner,
    CompanyImage,
    StaffImage,
)
from apps.company_description.serializers import (
    LinkSerializer,
    ContactSerializer,
    CompanyDescriptionSerializer,
    PatientInfoSerializer,
    ConstituentDocumentSerializer,
    PartnerSerializer,
    CompanyImageSerializer,
    StaffImageSerializer,
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
    queryset = CompanyDescription.objects.all()
    serializer_class = CompanyDescriptionSerializer
    http_method_names = ["get"]


class PatientInfoViewSet(viewsets.ModelViewSet):
    basename = "patient-info"
    queryset = ClientInfo.objects.all()
    serializer_class = PatientInfoSerializer
    http_method_names = ["get"]


class ConstituentDocumentViewSet(viewsets.ModelViewSet):
    basename = "constituent-document"
    queryset = ConstituentDocument.objects.all()
    serializer_class = ConstituentDocumentSerializer
    http_method_names = ["get"]


class PartnerViewSet(viewsets.ModelViewSet):
    basename = "partner"
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    http_method_names = ["get"]


class CompanyImageViewSet(viewsets.ModelViewSet):
    basename = "company-image"
    queryset = CompanyImage.objects.all()
    serializer_class = CompanyImageSerializer
    http_method_names = ["get"]


class StaffImageViewSet(viewsets.ModelViewSet):
    basename = "staff-image"
    queryset = StaffImage.objects.all()
    serializer_class = StaffImageSerializer
    http_method_names = ["get"]
