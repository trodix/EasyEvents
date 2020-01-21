from rest_framework import serializers
from api.models import (
    Event,
    EventDate,
    AttendeeType,
    Customer,
    EventOrder,
    EventTicket
)


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'address',
            'address_details',
            'zipcode',
            'city',
            'country',
            'event_dates',
            'attendee_types'
        ]
        depth = 1


class EventDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventDate
        fields = [
            'id',
            'event_date',
            'event'
        ]
        depth = 1


class AttendeeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AttendeeType
        fields = [
            'id',
            'name',
            'event_price',
            'vat_rate',
            'event'
        ]
        depth = 1


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'lastname',
            'firstname',
            'company_name',
            'phone',
            'email',
            'billing_address',
            'billing_zicode',
            'billing_city',
            'billing_country'
        ]
        depth = 1


class EventOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventOrder
        fields = [
            'order_date',
            'amount',
            'event',
            'customer'
        ]
        depth = 1


class EventTicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventTicket
        fields = [
            'ticket_number',
            'event',
            'attendeeType'
        ]
        depth = 1
