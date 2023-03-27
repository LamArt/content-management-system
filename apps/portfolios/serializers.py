from rest_framework import serializers

from apps.portfolios.models import Portfolio
from apps.seo.utils import PageSEOSerializerMixin


class PortfolioSerializerPage(PageSEOSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"
