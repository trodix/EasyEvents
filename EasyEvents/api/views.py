from api.models import Event, EventDate, AttendeeType
from rest_framework import viewsets, permissions
from api.serializers import EventSerializer, EventDateSerializer, AttendeeTypeSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventSerializer


class EventDateViewSet(viewsets.ModelViewSet):
    queryset = EventDate.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventDateSerializer


class AttendeeTypeViewSet(viewsets.ModelViewSet):
    queryset = AttendeeType.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AttendeeTypeSerializer
