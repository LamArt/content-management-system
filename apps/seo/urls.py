from django.urls import include, path
from rest_framework import routers

from apps.seo.views import PageSEOViewSet

router = routers.DefaultRouter()
router.register(r"page", PageSEOViewSet, basename=PageSEOViewSet.basename)

urlpatterns = [
    path("", include(router.urls)),
]
