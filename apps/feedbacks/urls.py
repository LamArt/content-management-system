from django.urls import path, include
from apps.feedbacks.views import FeedbackViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    r"feedback",
    FeedbackViewSet,
    basename=FeedbackViewSet.basename,
)

urlpatterns = [
    path("", include(router.urls)),
]
