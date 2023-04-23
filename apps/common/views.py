from django.shortcuts import render
from django.views import View

from apps.company_description.models import CompanyDescription


class IndexView(View):
    def get(self, request):
        clinic_description = CompanyDescription.objects.get()
        return render(
            request,
            "site/index.html",
            context={"clinic_description": clinic_description},
        )
