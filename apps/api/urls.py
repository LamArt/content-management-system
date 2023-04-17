from django.urls import path, include


urlpatterns = [
    path("services/", include("apps.services.urls")),
    path("portfolios/", include("apps.portfolios.urls")),
    path("clinic-info/", include("apps.company_description.api.urls")),
    path("common/", include("apps.common.api.urls")),
    path("feedbacks/", include("apps.feedbacks.urls")),
    path("feedback-forms/", include("apps.feedback_forms.urls")),
    path("employees/", include("apps.employees.urls")),
    path("seo/", include("apps.seo.urls")),
]
