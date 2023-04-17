from django.urls import include, path
from rest_framework import routers

from apps.company_description.api.views import (
    ContactViewSet,
    LinkViewSet,
    ClinicDescriptionViewSet,
    PatientInfoViewSet,
    ConstituentDocumentViewSet,
    InformedPatientConsentViewSet,
    MedicalProfessionalProvisionsViewSet,
    PartnerViewSet,
    ClinicImageViewSet,
    StaffImageViewSet,
)

router = routers.DefaultRouter()
router.register(r"contact", ContactViewSet, basename=ContactViewSet.basename)
router.register(r"link", LinkViewSet, basename=LinkViewSet.basename)
router.register(
    r"clinic-description",
    ClinicDescriptionViewSet,
    basename=ClinicDescriptionViewSet.basename,
)
router.register(
    r"patient-info", PatientInfoViewSet, basename=PatientInfoViewSet.basename
)
router.register(
    r"constituent-document",
    ConstituentDocumentViewSet,
    basename=ConstituentDocumentViewSet.basename,
)
router.register(
    r"informed-patient-consent",
    InformedPatientConsentViewSet,
    basename=InformedPatientConsentViewSet.basename,
)
router.register(
    r"medical-professional-provisions",
    MedicalProfessionalProvisionsViewSet,
    basename=MedicalProfessionalProvisionsViewSet.basename,
)
router.register(r"partner", PartnerViewSet, basename=PartnerViewSet.basename)
router.register(
    r"clinic-image", ClinicImageViewSet, basename=ClinicImageViewSet.basename
)
router.register(r"staff-image", StaffImageViewSet, basename=StaffImageViewSet.basename)

urlpatterns = [
    path("", include(router.urls)),
]
