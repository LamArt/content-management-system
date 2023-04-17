from django.urls import path, include

from apps.common.views import IndexView

urlpatterns = [path("", IndexView.as_view())]
