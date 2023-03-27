from rest_framework import viewsets

from apps.seo.models import PageSEO
from apps.seo.serializers import PagePageSEOSerializer


class PageSEOViewSet(viewsets.ModelViewSet):
    basename = "page"
    queryset = PageSEO.objects.all()
    serializer_class = PagePageSEOSerializer
    http_method_names = ["get"]
