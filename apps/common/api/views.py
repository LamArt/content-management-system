from django.apps import apps
from rest_framework.response import Response
from rest_framework.views import APIView


class LastUpdateTimeApi(APIView):
    name = "last-update-time"

    def get(self, request):
        last_time_update = None
        for app in apps.get_app_configs():
            for model in app.get_models():
                try:
                    last_time_update_model = model.objects.latest(
                        "updated_at"
                    ).updated_at
                    if not last_time_update:
                        last_time_update = last_time_update_model
                    if last_time_update_model > last_time_update:
                        last_time_update = last_time_update_model
                except BaseException:  # except FieldError or model.DoesNotExist
                    pass
        return Response({"last_update_time": last_time_update})
