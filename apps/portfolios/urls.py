from django.urls import include, path
from rest_framework import routers

from apps.portfolios.views import PortfolioViewSetPage

router = routers.DefaultRouter()
router.register(
    r"portfolio", PortfolioViewSetPage, basename=PortfolioViewSetPage.basename
)

urlpatterns = [
    path("", include(router.urls)),
]
