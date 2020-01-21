from rest_framework import viewsets
from api.models import (
    Event,
    EventDate,
    AttendeeType,
    Customer,
    EventOrder,
    EventTicket
)
from api.serializers import (
    EventSerializer,
    EventDateSerializer,
    AttendeeTypeSerializer,
    CustomerSerializer,
    EventOrderSerializer,
    EventTicketSerializer
)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDateViewSet(viewsets.ModelViewSet):
    queryset = EventDate.objects.all()
    serializer_class = EventDateSerializer


class AttendeeTypeViewSet(viewsets.ModelViewSet):
    queryset = AttendeeType.objects.all()
    serializer_class = AttendeeTypeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EventOrderViewSet(viewsets.ModelViewSet):
    queryset = EventOrder.objects.all()
    serializer_class = EventOrderSerializer


class EventTicketViewSet(viewsets.ModelViewSet):
    queryset = EventTicket.objects.all()
    serializer_class = EventTicketSerializer
