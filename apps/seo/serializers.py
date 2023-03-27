from rest_framework import serializers

from apps.seo.models import PageSEO
from apps.seo.utils import PageSEOSerializerMixin


class PagePageSEOSerializer(PageSEOSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = PageSEO
        fields = "__all__"
