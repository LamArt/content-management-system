from django.urls import include, path
from rest_framework import routers

from apps.feedback_forms.views import (
    FeedBackFormViewSet,
    LogViewSet,
    FeedbackFormFieldsApi,
)

router = routers.DefaultRouter()
router.register(
    r"feedback-form", FeedBackFormViewSet, basename=FeedBackFormViewSet.basename
)
router.register(r"log", LogViewSet, basename=LogViewSet.basename)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "feedback-form/<int:pk>/fields/",
        FeedbackFormFieldsApi.as_view(),
        name=FeedbackFormFieldsApi.name,
    ),
]
