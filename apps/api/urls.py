from django.urls import path, include


urlpatterns = [
    path("services/", include("apps.services.urls")),
    path("portfolios/", include("apps.portfolios.urls")),
    path("company-description/", include("apps.company_description.urls")),
    path("common/", include("apps.common.urls")),
    path("feedbacks/", include("apps.feedbacks.urls")),
    path("feedback-forms/", include("apps.feedback_forms.urls")),
    path("employees/", include("apps.employees.urls")),
    path("seo/", include("apps.seo.urls")),
]
