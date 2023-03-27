from rest_framework import serializers

from apps.feedback_forms.models import FeedbackForm, Field, FeedbackFormLog


class FeedBackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = "__all__"


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        depth = 1
        exclude = ("feedback_forms",)


class FeedbackFormLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackFormLog
        fields = "__all__"
