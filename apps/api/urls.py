from django.urls import path, include


urlpatterns = [
    path("contacts/", include("apps.contacts.urls")),
    path("common/", include("apps.common.urls")),
]
