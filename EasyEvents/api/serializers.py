from rest_framework import serializers
from api.models import Event, EventDate, AttendeeType


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'address', 'address_details', 'zipcode', 'city', 'country', 'event_dates', 'attendee_types']
        depth = 1


class EventDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventDate
        fields = ['id', 'event_date', 'event']
        depth = 1


class AttendeeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AttendeeType
        fields = ['id', 'name', 'event_price', 'vat_rate', 'event']
        depth = 1
