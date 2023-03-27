from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.feedback_forms.models import FeedbackForm, FeedbackFormLog
from apps.feedback_forms.serializers import (
    FeedBackFormSerializer,
    FieldSerializer,
    FeedbackFormLogSerializer,
)
from apps.feedback_forms.services import send_confirmation_email, send_manager_email


class FeedBackFormViewSet(viewsets.ModelViewSet):
    basename = "feedback-form"
    queryset = FeedbackForm.objects.all()
    serializer_class = FeedBackFormSerializer
    http_method_names = ["get"]


class LogViewSet(viewsets.ModelViewSet):
    basename = "feedback-form-log"
    queryset = FeedbackFormLog.objects.all()
    serializer_class = FeedbackFormLogSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        feedback_form_log = get_object_or_404(FeedbackFormLog, id=response.data["id"])

        if feedback_form_log.feedback_form.confirmation_email:
            send_confirmation_email(feedback_form_log)
        send_manager_email(feedback_form_log)

        return response


class FeedbackFormFieldsApi(APIView):
    name = "feedback-form-fields"

    def get(self, request, pk):
        qs = FeedbackForm.objects.get(id=pk)
        return Response({"fields": FieldSerializer(qs.fields.all(), many=True).data})
