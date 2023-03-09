from django.urls import include, path
from rest_framework import routers

from apps.contacts.views import ContactViewSet, LinkViewSet

router = routers.DefaultRouter()
router.register(r"contact", ContactViewSet, basename=ContactViewSet.basename)
router.register(r"link", LinkViewSet, basename=LinkViewSet.basename)

urlpatterns = [
    path("", include(router.urls)),
]
