from rest_framework import viewsets

from apps.feedbacks.models import Feedback

from apps.feedbacks.serializers import FeedbackSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    basename = "feedback"
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    http_method_names = ["get"]
