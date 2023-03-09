from rest_framework import viewsets

from apps.contacts.models import Link, Contact
from apps.contacts.serializers import LinkSerializer, ContactSerializer


class LinkViewSet(viewsets.ModelViewSet):
    basename = "link"
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    http_method_names = ["get"]


class ContactViewSet(viewsets.ModelViewSet):
    basename = "contact"
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ["get"]
