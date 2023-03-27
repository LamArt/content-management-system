from rest_framework import viewsets

from apps.portfolios.models import Portfolio
from apps.portfolios.serializers import PortfolioSerializerPage
from apps.seo.utils import PageSEOViewMixin


class PortfolioViewSetPage(PageSEOViewMixin, viewsets.ModelViewSet):
    basename = "portfolio"
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializerPage
    http_method_names = ["get"]
