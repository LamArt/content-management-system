from django.urls import path

from apps.common.api.views import LastUpdateTimeApi


urlpatterns = [
    path("last-update-time/", LastUpdateTimeApi.as_view(), name=LastUpdateTimeApi.name),
]
