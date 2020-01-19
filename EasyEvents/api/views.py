from api.models import Event, EventDate, AttendeeType
from rest_framework import viewsets
from api.serializers import EventSerializer, EventDateSerializer, AttendeeTypeSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDateViewSet(viewsets.ModelViewSet):
    queryset = EventDate.objects.all()
    serializer_class = EventDateSerializer


class AttendeeTypeViewSet(viewsets.ModelViewSet):
    queryset = AttendeeType.objects.all()
    serializer_class = AttendeeTypeSerializer
