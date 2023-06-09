from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from content_management_system.settings import env

admin.site.site_title = "CMS"
admin.site.site_header = "CMS | Панель Администратора"
admin.site.site_url = env.get_value("FRONTEND_SITE_URL")


schema_view = get_schema_view(
    openapi.Info(
        title="CMS API",
        default_version="v1",
        description="Backend for content-management-system",
        contact=openapi.Contact(email="inbox@lamart.site"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/", include("apps.api.urls")),
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
