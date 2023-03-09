from rest_framework import serializers

from apps.contacts.models import Contact, Link


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
