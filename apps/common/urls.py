from django.urls import path

from apps.common.views import LastUpdateTimeApi


urlpatterns = [
    path("last-update-time/", LastUpdateTimeApi.as_view(), name=LastUpdateTimeApi.name),
]
